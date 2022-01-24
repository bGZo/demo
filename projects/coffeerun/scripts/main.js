(function(window) {
    'use stricts';
    var FORM_SELECTOR = '[data-coffee-order="form"]'; //FormHandle parameter
    var CHECKLIST_SELECTOR = '[data-coffee-order="checklist"]';

    var App=window.App;
    var Truck =App.Truck;
    var DataStore = App.DataStore;

    var FormHandler = App.FormHandler;
    var CheckList  = App.CheckList;
    var myTruck = new Truck('ncc-1701', new DataStore());

    window.myTruck=myTruck; // push Truck to global space
    var checkList = new CheckList(CHECKLIST_SELECTOR);
    var formHandler = new FormHandler(FORM_SELECTOR);

    formHandler.addSubmitHandler(function(data) { // this place!!
        myTruck.createOrder.call(myTruck, data);
        checkList.addRow.call(checkList, data);
    });/* formHandler.addSubmitHandler(checkList.addRow.bind(checkList));
        * following stmt not work cause the callback will reset data before addRow
        */

    formHandler.addSubmitHandler(myTruck.createOrder.bind(myTruck));
    // formHandler.addSubmitHandler(function(data) {
    //     myTruck.createOrder.call(myTruck, data);
    // });
    /* formHandler.addSubmitHandler(myTruck.createOrder());
     * will not work cause the owner changed, must use bind to link createOrder to myTrack
     * ???
     */

    console.log(formHandler);
})(window);