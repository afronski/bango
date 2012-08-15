onload = function(d)
{
	var emots = 	{ ':)':'Smile.png',
			  ':-)':'Smile.png',
				  
			  ';)':'Smile.png',
			  ';-)':'Smile.png',

			  ':p':'Tongue.png',
			  ':P':'Tongue.png',
			  ':-P':'Tongue.png',
			  ':-p':'Tongue.png',

			  ';p':'Tongue2.png',
			  ';P':'Tongue2.png',
			  ';-P':'Tongue2.png',
			  ';-p':'Tongue2.png',

			  '8-)':'Cool.png',			  

			  ':*':'Kiss.png',
			  ':-*':'Kiss.png',			  

			  ':(':'Sad.png',
			  ':-(':'Sad.png',

			  ';-(':'Cry.png',
			  ';(':'Cry.png',

			  ':D':'Lol.png',
			  ':d':'Lol.png',
			  ':-D':'Lol.png',			  
			  ':-d':'Lol.png',
			
			  ']:->':'Devil.png',
			  ':devil:':'Devil.png',

		          ':geek:':'Geek.png',

			  ':alien:':'Alien.png',

  			  ':evil:':'Evil.png',

			  ':info:':'Info.png'
			}

	var dir = '/media/emoticons/';

	d = document.body;
	for (var i in emots)
	{
		d.innerHTML = 
		d.innerHTML.replace(RegExp(i.replace(/([(\\)?*+.^])/g, '\\' + '$1').replace(/>/g,'&gt;'), 'g'), 
					   '<img src = "' + dir + emots[i] + '" alt = "' + emots[i]+ '" style = "border:0;vertical-align:middle" />');
	}
}	
