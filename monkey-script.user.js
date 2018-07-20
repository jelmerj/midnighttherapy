// ==UserScript==
// @name       Pathery Assist
// @namespace  https://github.com/WuTheFWasThat/midnighttherapy
// @version    0.2
// @description  Assistance for playing Pathery
// @match      https://www.pathery.com/home
// @match      https://www.pathery.com/mapeditor*
// @match      https://www.pathery.com/scores*
// @match      https://www.pathery.com/
// @match      https://beta.pathery.net/home
// @match      https://beta.pathery.net/mapeditor*
// @match      https://beta.pathery.net/scores*
// @match      https://beta.pathery.net/
// @match      http://beta.pathery.net/home
// @match      http://beta.pathery.net/mapeditor*
// @match      http://beta.pathery.net/scores*
// @match      http://beta.pathery.net/
// @match      https://blue.pathery.net/home
// @match      https://blue.pathery.net/mapeditor*
// @match      https://blue.pathery.net/scores*
// @match      https://blue.pathery.net/
// @match      http://blue.pathery.net/home
// @match      http://blue.pathery.net/mapeditor*
// @match      http://blue.pathery.net/scores*
// @match      http://blue.pathery.net/
// @match      http://pathery.unbridled.eu/home
// @match      http://pathery.unbridled.eu/mapeditor*
// @match      http://pathery.unbridled.eu/scores*
// @match      http://pathery.unbridled.eu/
// @match      https://pathery.unbridled.eu/home
// @match      https://pathery.unbridled.eu/mapeditor*
// @match      https://pathery.unbridled.eu/scores*
// @match      https://pathery.unbridled.eu/

// @copyright  2012+, You
// @grant      none
// ==/UserScript==


// IF YOU'RE NOT RUNNING A SERVER:
var url = 'https://raw.githubusercontent.com/WuTheFWasThat/midnighttherapy/master/pathery-full.js';

// ALTERNATIVELY, IF YOU ARE RUNNING A SERVER:
//mt_local_testing = true;
//mt_url='http://127.0.0.1:2222/'  // OR WHATEVER YOUR SERVER IS
//var url = mt_url + 'pathery-client.js'

$.ajax({
  url: url,
  type: 'GET',
  dataType: 'text',
  success: function(data) { eval(data); },
});
