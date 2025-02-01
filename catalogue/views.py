from django.shortcuts import render, get_object_or_404, redirect
from .models import CatalogueItem, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def catalogue_home(request):
    """
    Displays all items available in the catalogue.

    **Template:**
    - catalogue/catalogue.html
    """
    catalogue_items = CatalogueItem.objects.all()
    return render(
        request,
        'catalogue/catalogue.html',
        {'catalogue_items': catalogue_items}
        )


@login_required
def catalogue_detail(request, slug):
    """
    Displays detailed information for the item selected.

    ** Context:**
    - `selected_item` : The item retrieved based on its slug.

    **Template:**
    - catalogue/catalogue_detail.html
    """
    selected_item = get_object_or_404(
        CatalogueItem, 
        slug=slug
        )
    return render(
        request,
        'catalogue/catalogue_detail.html',
        {'selected_item': selected_item}
        )


# Cart-related views
@login_required
def cart_page(request):
    """
    Displays the user's cart, including details like image, name, 
    quantity, and total points cost.

    **Context:**
    - `cart_items`: Items in the user's cart.
    - `total_points_cost`: Total points cost for all items in the cart.
    - `user_balance`: The user's current points balance.
    - `balance_sufficient`: If the user has enough points for redemption.
    - `missing_points`: The points needed if balance is insufficient.

    **Template:**
    - catalogue/cart.html

    """
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all() if cart else []
    total_points_cost = sum(
        item.total_points() for item in cart_items
        )
    user_balance = request.user.userprofile.point_balance
    balance_sufficient = user_balance >= total_points_cost
    missing_points = (
        total_points_cost - user_balance
        if not balance_sufficient
        else 0
    )

    return render(request, 'catalogue/cart.html', {
        'cart_items': cart_items,
        'total_points_cost': total_points_cost,
        'user_balance': user_balance,
        'balance_sufficient': balance_sufficient,
        'missing_points': missing_points,
    })


@login_required
def add_to_cart(request, slug):
    """
    Adds a new CartItem to the cart for the current user (Create functionality).

    **Context:**
    - `slug`: The slug of the CatalogueItem to be added to the cart.
    - `cart`: The user's cart instance, created if it doesn't exist.
    - `cart_item`: The specific CartItem being added or updated.

    **Flow**
    - Accepts a POST request.
    - Retrieves or creates the cart for the user.
    - Creates a new CartItem in the database OR increase quantity.
    - Redirects to the catalogue_detail page.

    **Redirect:**
    - catalogue/catalogue_detail.html
    """
    if request.method == "POST":
        item = get_object_or_404(CatalogueItem, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item
            )
        if created:
            messages.success(request, f"{item.reward_name} has been added to your cart!")
        else:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f"{item.reward_name} quantity updated in your cart!")

        return redirect('catalogue_detail', slug=item.slug)

    return redirect('catalogue_detail', slug=slug)


@login_required
def update_cart_quantity(request, slug):
    """
    Updates the quantity of an existing item in the cart.

    **Context:**
    - `slug`: The slug of the CatalogueItem to be updated in the cart.
    - `cart_item`: The specific CartItem being updated.

    **Flow:**
    - Accepts a POST request with a new quantity.
    - Updates the CartItem's quantity or deletes it if the quantity is < 1.
    - Redirects to the cart page.

    **Redirect:**
    - catalogue/cart.html
    """
    if request.method == 'POST':
            # Get the item and cart_item for the current user
            item = get_object_or_404(CatalogueItem, slug=slug)
            cart_item = get_object_or_404(
                CartItem,
                cart__user=request.user,
                item=item
                )

            # Parse and validate the new quantity
            new_quantity = int(request.POST.get('quantity', 1))
            if new_quantity < 1:
                cart_item.delete()
            else:
                cart_item.quantity = new_quantity
                cart_item.save()

    return redirect('cart_page')


@login_required
def delete_cart_item(request, slug):
    """
    Deletes an existing item from the user's cart.

    **Context:**
    - `slug`: The slug of the CatalogueItem to be deleted from the cart.
    - `cart_item`: The CartItem instance being removed.

    **Flow:**
    - Accepts a POST request to delete a specific cart item.
    - Retrieves the CartItem associated with the slug and the user's cart.
    - Deletes the CartItem from the database.
    - Redirects back to the cart page.

    **Redirect:**
    - catalogue/cart.html
    """
    if request.method == 'POST':
        # Find the cart item to delete
        cart_item = get_object_or_404(
            CartItem,
            cart__user=request.user,
            item__slug=slug
            )
        cart_item.delete()

    return redirect('cart_page')


@login_required
def redeem_cart(request):
    """
    Handles the redemption process for the user's cart.

    **Context:**
    - `cart`: The user's Cart instance, retrieved or created.
    - `cart_items`: The list of CartItem instances in the user's cart.
    - `total_points_cost`: The total points required for all items in the cart.
    - `user_profile`: The user's UserProfile instance for managing point balance.

    **Flow:**
    - Retrieves the user's cart and associated items.
    - Validates the user's point balance to ensure sufficient points.
    - Deducts points from the user's balance upon successful redemption.
    - Clears all items from the cart.
    - Adds success or error messages using Django's messages.
    - Redirects to the cart page.

    **Redirect:**
    - catalogue/cart.html
    """
    if request.method == 'POST':
        # Get or create the user's cart
        cart, _ = Cart.objects.get_or_create(user=request.user)
        # Fetch cart items
        cart_items = cart.cartitem_set.all()
        # Calculate total points cost
        total_points_cost = sum(item.total_points() for item in cart_items)

        # Validate the user's balance
        user_profile = request.user.userprofile
        if user_profile.point_balance < total_points_cost:
            # Add error message
            messages.error(request, "You don't have enough points to redeem.")
            return redirect('cart_page')
        
        # Deduct points from the user's balance
        user_profile.point_balance = (
            user_profile.point_balance - total_points_cost
            )
        user_profile.save()
        # Clear cart
        cart.cartitem_set.all().delete()

        # Add success message
        messages.success(
            request, 
            "Redemption successful! Your cart has been cleared."
            )
        
        # Redirect after successful redemption
        return redirect('cart_page')
    
    return redirect('cart_page')