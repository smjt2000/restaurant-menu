const filterMenuItems = (_filter) => {
	const container = document.querySelector('.food-cards');

	// Build the URL with the category parameter
	let url = '/api/filter?fltr=';
	if (_filter) {
		url += `${encodeURIComponent(_filter)}`;
	}

	fetch(url)
		.then(response => {
			return response.json()
		})
		.then(data => {
			// Clear the container
			container.innerHTML = '';
			// Render the menu items
			data.forEach((item, i) => {
				const itemHTMLconst = `

                            <div class="card">

								<div class="right">
									<img src="${item.thumbnail}" alt="${item.title}">
								</div>
								<div class="left">
									<div dir="rtl">
										<h2>${item.title}</h2>
										<p class="truncate">${item.description}</p>
									</div>
									<hr/>
									<span>${item.persian_digit_price} تومان</span>
								</div>
                            </div>
                        `;
				container.innerHTML += itemHTMLconst;
			});

			// Show a message if no items are found
			if (data.length === 0) {
				container.innerHTML = '<p>No items found for this category.</p>';
			}
		})
		.catch(error => {
			console.error('Error fetching menu items:', error);
			container.innerHTML = '<p>Failed to load menu items.</p>';
		});
}

const fetchMenuItems = (category) => {
	// Show a loading message
	const container = document.querySelector('.food-cards');

	// Build the URL with the category parameter
	let url = '/api/category?search=';
	if (category) {
		url += `${encodeURIComponent(category)}`;
	}

	// Send the AJAX request
	fetch(url)
		.then(response => {
			return response.json()
		})
		.then(data => {
			// Clear the container
			container.innerHTML = '';
			// Render the menu items
			data.forEach((item, i) => {
				const itemHTMLconst = `
				<div class="card">
				<div class="right">
				<img src="${item.thumbnail}" alt="${item.title}">
				</div>
				<div class="left">
				<div dir="rtl">
				<h2>${item.title}</h2>
				<p class="truncate">${item.description}</p>
				</div>
				<hr/>
				<span>${item.persian_digit_price} تومان</span>
				</div>
				</div>
                        `;
				container.innerHTML += itemHTMLconst;
			});

			// Show a message if no items are found
			if (data.length === 0) {
				container.innerHTML = '<p>No items found for this category.</p>';
			}
		})
		.catch(error => {
			console.error('Error fetching menu items:', error);
			container.innerHTML = '<p>Failed to load menu items.</p>';
		});
}

filterMenuItems('_all');
