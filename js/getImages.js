var _mainContainer = document.getElementById('gallery');

var data;
if(data !== undefined)
{
	let _counter = 0;
	Object.keys(data).forEach(key => {
		let _y = key.substring(0,4);
		let _m = key.substring(4,6)
		let _d = key.substring(6,8)

		let _container = document.createElement('DIV');
		_mainContainer.appendChild(_container);

		let _h3 = document.createElement("H3");
		let _text = document.createTextNode(_m + '/' + _d + '/' + _y);
		_container.appendChild(_h3);
		_h3.appendChild(_text);

		if((_counter++)%2 == 0) {
			_container.className = 'p-4 date-container bg-secondary'
		} else {
			_container.className = 'p-4 date-container bg-dark'
			_h3.className = 'text-light'
		}

		let _row;
		for(i in data[key])
		{
			if(i%4 == 0)
			{
				_row = document.createElement('DIV');
				_row.className = 'row';
				_container.appendChild(_row);
			}

			let _imgContainer = document.createElement('DIV');
			_imgContainer.className = 'image-container col-sm-3 p-5 align-self-center';

			let _img = document.createElement("IMG");
			_img.src = '../' + data[key][i];
			_img.onload = _ => (_img.className = _img.width > _img.height ? 'wide' : 'tall');

			_row.appendChild(_imgContainer);
			_imgContainer.appendChild(_img);
		}

	});
}