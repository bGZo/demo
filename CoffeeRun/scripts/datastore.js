/*
 * IIFE: 立即调用函数表达式
 * see more: https://developer.mozilla.org/zh-CN/docs/Glossary/IIFE
 * (function () { statements })();
 * create namespace for hugo code
 */
(function(window) {
    'use strict';
    var App=window.App || {}; 
    // a test for old object
    // if app exists, assign it to local App
    // else use {} meaning that's a void object 

    function DataStore(){
        // console.log('running the DataStore function');
        this.data={}; 
        /* constructor, just like cpp?
         * escapically use new which returns a implicit object
         * 
         * after writing following add, get and remove function
         * we could save data though this type
         */
    };

    DataStore.prototype.add = function (key, val){
        this.data[key]=val;
        /* once use the new stmt, the prototype will also use.
         * and every created by this constructor will be able
         * to use this add function.
         * 
         * By the way, javascript make the key value unique.
         */
    };

    DataStore.prototype.get = function (key){
        return this.data[key];
    };

    DataStore.prototype.getAll = function (){
        return this.data;
    }

    DataStore.prototype.remove = function (key){
        delete this.data[key];
    };

    App.DataStore = DataStore;
    window.App = App;
    // add a DataStore assign to App object
    // then use configed app assign to global environment.
})(window);