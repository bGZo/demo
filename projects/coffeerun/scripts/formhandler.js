(function(window) {
    'use strict';
    var App = window.App || {};
    var $ = window.jQuery;

    function FormHandler(selector){
        /* selector means use all form.
        */
       if(!selector){// check the selector is not null which jquery not support.
           throw new Error('No selector provided!');
       }

       this.$formELement = $(selector);
       /* Jquiry return the whole object indcluded the quoto of the element of DOM.
        */

       if(this.$formELement.length === 0){
           throw new Error('Could not find element with selector: ' + selector);
       }
    }

    FormHandler.prototype.addSubmitHandler = function (fn){
        console.log('Setting submit handler for form');
        this.$formELement.on('submit', function(event){
            event.preventDefault();// ensure user not leaving the page.
            
            var data= {};//$(this).serializeArray();//jquery support to get the form data

            $(this).serializeArray().forEach(function(item) {
                data[item.name]=item.value;
                console.log(item.name+' is '+item.value);
            });// to serializeArray() use the callback function
            console.log(data);
            fn(data);

            this.reset();// next order
            this.elements[0].focus();
        })
    };
    
    App.FormHandler = FormHandler;
    window.App = App;

})(window);