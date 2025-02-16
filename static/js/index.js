const bottomSheet = document.querySelector(".bottom-sheet");
const sheetOverlay = bottomSheet.querySelector(".sheet-overlay");
const sheetContent = bottomSheet.querySelector(".content");
const dragIcon = bottomSheet.querySelector(".drag-icon");

let isDragging = false,
	startY, startHeight;
const hideBottomSheet = () => {
	bottomSheet.classList.remove("show");
	document.body.style.overflowY = "auto";
};

const updateSheetHeight = (height) => {
	sheetContent.style.height = `${height}vh`;
	bottomSheet.classList.toggle("fullscreen", height === 100);
};

const showBottomSheet = () => {
	bottomSheet.classList.add("show");
	document.body.style.overflowY = "hidden";
	updateSheetHeight(70); // Default to 50% height
};

const showDetails = (id) => {
	let url = '/api/item?id=';
	if (id) {
		url += `${encodeURIComponent(id)}`;
	}
	fetch(url)
		.then(response => {
			return response.json()
		})
		.then(data => {
			document.getElementById("modalItemName").innerText = data.title;
			document.getElementById("modalItemDescription").innerText = data.description;
			document.getElementById("modalItemCategory").innerText = `دسته‌بندی: ${data.categories.title}`;
			document.getElementById("modalItemPrice").innerText = `قیمت: ${data.persian_digit_price}`;
			document.getElementById("modalItemImg").src = data.thumbnail;
			showBottomSheet();
			if (data.length === 0) {
				console.log("No items found");
			}
		})
		.catch(error => {
			console.error('Error fetching menu items:', error);
		});
}

const dragStart = (e) => {
	isDragging = true;
	startY = e.pageY || e.touches?.[0].pageY;
	startHeight = parseInt(sheetContent.style.height);
	bottomSheet.classList.add("dragging");
};

const dragging = (e) => {
	if (!isDragging) return;
	const delta = startY - (e.pageY || e.touches?.[0].pageY);
	const newHeight = startHeight + delta / window.innerHeight * 100;
	updateSheetHeight(newHeight);
};

const dragStop = () => {
	isDragging = false;
	bottomSheet.classList.remove("dragging");
	const sheetHeight = parseInt(sheetContent.style.height);
	sheetHeight < 25 ? hideBottomSheet() : sheetHeight > 75 ? updateSheetHeight(100) : updateSheetHeight(50);
};

// Attach event listeners
dragIcon.addEventListener("mousedown", dragStart);
document.addEventListener("mousemove", dragging);
document.addEventListener("mouseup", dragStop);

dragIcon.addEventListener("touchstart", dragStart);
document.addEventListener("touchmove", dragging);
document.addEventListener("touchend", dragStop);

sheetOverlay.addEventListener("click", hideBottomSheet);




const filterMenuItems = (_filter) => {
	const container = document.getElementById('menu');

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
                            <div class="col-md-4 mb-3">
                                <div class="card" onclick="showDetails('${item.id}')">
                                    <img src="${item.thumbnail}" alt="${item.title}">
                                    <div class="card-body">
                                        <h5 class="card-title">${item.title}</h5>
                                        <p class="card-text mb-1"><strong>دسته‌بندی:</strong> ${item.categories.title}</p>
                                        <p class="card-text mb-1" style="font-size: .7rem;">${item.description}</p>
                                        <p class="text-muted mb-0" style="font-size: .65rem;">${item.persian_digit_price} تومان</p>
                                    </div>
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
	const container = document.getElementById('menu');

	// Build the URL with the category parameter
	let url = '/api/category?search=';
	console.log(category)
	if (category) {
		url += `${encodeURIComponent(category)}`;
	}
	console.log(url);

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
                            <div class="col-md-4 mb-3">
                                <div class="card" onclick="showDetails('${item.id}')">
                                    <img src="${item.thumbnail}" alt="${item.title}">
                                    <div class="card-body">
                                        <h5 class="card-title">${item.title}</h5>
                                        <p class="card-text mb-1"><strong>دسته‌بندی:</strong> ${item.categories.title}</p>
                                        <p class="card-text mb-1" style="font-size: .7rem;">${item.description}</p>
                                        <p class="text-muted mb-0" style="font-size: .65rem;">${item.persian_digit_price} تومان</p>
                                    </div>
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

// Add an event listener to the category dropdown
document.getElementById('category').addEventListener('change', function() {
	const selectedCategory = this.value;
	fetchMenuItems(selectedCategory);
});
