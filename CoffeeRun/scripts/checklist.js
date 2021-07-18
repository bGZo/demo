(function(window){
    'use strict';

    var App = window.App || {};
    var $ = window.jQuery;

    function CheckList(selector){
        if(!selector){
            throw new Error('No Selector provided!');
        }

        this.$element = $(selector);
        if(this.$element.length === 0){
            throw new Error('Could not find element with selectir: ' + selector);
        }
    }

    CheckList.prototype.addRow = function (coffeeOrder) {
        // remove same email row
        // this.removeRow(coffeeOrder.emailAddress);

        var rowElement = new Row(coffeeOrder);
        // use coffee order create new Row example

        this.$element.append(rowElement.$element);
        // add new Row 's $element property to order
    };

    CheckList.prototype.removeRow = function (email) {
        this.$element
        .find('value="' + email +'"]')
        .closest('[data-coffee-order="checkbox"]')
        .remove();
    };

    function Row(coffeeOrder){
        var $div = $( '<div></div>',{
            'data-coffee-order':'checkbox',
            'class':'checkbox'
        });

        var $label = $('<label></label>')

        var $checkbox = $('<input></input>',{
            type: 'checkbox',
            value: coffeeOrder.email 
        });/*emailAddress is work for what????*/

        var description = coffeeOrder.size + ' ';
        if(coffeeOrder.flavor){
            description += coffeeOrder.flavor + ' ';
        }
        description += coffeeOrder.coffee + ', ';
        description += ' (' + coffeeOrder.email + ') ';/*why emailAddress is not work*/
        description += ' [' + coffeeOrder.strength + 'x] ';

        $label.append($checkbox);
        $label.append(description);
        $div.append($label);

        this.$element = $div; 
        /*constructor never use return, so use property to return this tree */
    }

    App.CheckList = CheckList;
    window.App = App;

})(window);