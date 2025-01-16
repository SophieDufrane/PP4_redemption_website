from django.shortcuts import render, get_object_or_404, redirect
from .models import CatalogueItem, Cart, CartItem
from django.contrib.auth.decorators import login_required


@login_required
def catalogue_home(request):
    """
    Displays all items available in catalogue.
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
    """
    selected_item = get_object_or_404(CatalogueItem, slug=slug)
    return render(
        request,
        'catalogue/catalogue_detail.html',
        {'selected_item': selected_item}
        )


@login_required
def cart_page(request):
    """
    Displays the user's cart and total points cost.

    **Context**

    - `cart_items`: List of items in the user's cart.
    - `total_points_cost`: Total points cost for all items in the cart.

    **Template**

    - catalogue/cart.html

    """
    # Get cart for the current user (1st object or None)
    cart = Cart.objects.filter(user=request.user).first()
    # Fetch cart items if exists, else an empty cart
    cart_items = cart.cartitem_set.all() if cart else []
    total_points_cost = sum(
        item.item.points_cost * item.quantity for item in cart_items
        )

    return render(request, 'catalogue/cart.html', {
        'cart_items': cart_items,
        'total_points_cost': total_points_cost
    })


@login_required
def add_to_cart(request, slug):
    """
    Adds an item to the cart for the current session or user.

    **Context**

    - `slug`: Slug of the CatalogueItem to add to cart.

    **Flow**

    - Only allow adding items via a POST request.
    - Fetch the item to add using the slug of the `CatalogueItem`.
    - Retrieve or create the cart.
    - Add the item to the cart OR increase the quantity if it already exists.
    - Redirect to the catalogue_detail page.
    """
    if request.method == "POST":
        item = get_object_or_404(CatalogueItem, slug=slug)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item
            )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('catalogue_detail', slug=item.slug)

    return redirect('catalogue_detail', slug=slug)


@login_required
def update_cart_quantity(request, slug):
    """
    Update the quantity of an existing item in the cart.

    **Flow**

    - Accepts a POST request with the new quantity.
    - Finds the `CartItem` using the slug of the `CatalogueItem`.
    - Updates the quantity of the `CartItem` if valid.
    - Redirects back to the cart page.
    """
    if request.method == 'POST':
            # Get the item and cart_item for the current user
            item = get_object_or_404(CatalogueItem, slug=slug)
            cart_item = get_object_or_404(CartItem, cart__user=request.user, item=item)

            # Parse and validate the new quantity
            new_quantity = int(request.POST.get('quantity', 1))
            if new_quantity < 1:
                cart_item.delete()
            else:
                cart_item.quantity = new_quantity
                cart_item.save()

    return redirect('cart_page')