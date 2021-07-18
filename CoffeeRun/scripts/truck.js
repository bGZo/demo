(function(window){
    'use strict';
    var App=window.App || {};

    function Truck(truckId, db){
        /* constructor
         * db uses DataStore build by datastore.js
         */
        this.truckId = truckId;
        this.db = db;
    };

    Truck.prototype.createOrder = function (order){
        console.log('Adding order for' + order.emailAddress);
        this.db.add(order.emailAddress, order);
    };

    Truck.prototype.deliverOrder = function(customerId){
        console.log('Delivering order for'+ customerId);
        this.db.remove(customerId); 
    };

    Truck.prototype.printOrders = function (){
        var customerIdArray = Object.keys(this.db.getAll());
        console.log('Truck #' + this.truckId + 'has pending orders:');
        customerIdArray.forEach(function(id){
            console.log(this.db.get(id));
            /* Callback function didn't have owner, so should use
             * bind method to link objecter to this.
             */
        }.bind(this));
        /* this meaning the example Truck. so firstly execute bind then
         * execute foreach
         */
    };

    App.Truck = Truck;
    window.App = App;// add trunk to global app
    // not cover data??? -> no
})(window);