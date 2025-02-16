const tableName = JSON.parse(document.getElementById('table-name').textContent);

const chatSocket = new WebSocket(
	'ws://' +
	window.location.host +
	'/ws/chat/' +
	tableName +
	'/'
);

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
};

document.querySelector('#call').onclick = function(e) {
	chatSocket.send(JSON.stringify({
		'table_name': tableName
	}));
};

window.addEventListener('load', () => {
	const urlSearchParams = window.location.search
	const searchParams = new URLSearchParams(urlSearchParams)

	const tableName = searchParams.get("table_name")
	if (tableName && tableName !== 'admin') {
		Cookies.set('table_name', tableName)
		searchParams.delete("table_name")
		window.history.replaceState({}, '', window.location.pathname);
		//window.location.reload();
	}
})
