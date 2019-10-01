var _div = document.getElementById('image_container');

// var _el = document.createElement("IMG");
// _el.src = './media/20160613/1370ML0067050020601164D01_DXXX.jpg'
// _div.appendChild(_el)

var data;
if(data !== undefined)
{
	key = Object.keys(data)[0]
	for(i in data[key])
	{
		console.log(data[key][i])
	}
}