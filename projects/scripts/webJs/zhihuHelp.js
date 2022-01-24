// ==UserScript==
// @name         Zhihu Demo
// @namespace    http://tampermonkey.net/
// @version      0.1.0
// @match        https://*zhihu.com*
// @icon         https://www.google.com/s2/favicons?domain=zhihu.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }
    sleep(2000).then(() => {
        document.getElementsByClassName('Button Modal-closeButton Button--plain')[0].click();
    })
})();