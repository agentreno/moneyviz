(function(){
   var app = angular.module('moneyviz', ['ui.router', 'ngAnimate']);
   app.config(function($stateProvider, $urlRouterProvider){
      $urlRouterProvider.otherwise('/');
      $stateProvider
         .state('home', {
            url: '/',
            templateUrl: 'partials/home.html',
         })
         .state('balance', {
            url: '/',
            templateUrl: 'partials/balance.html',
         })
         .state('account-personal', {
            url: '/',
            templateUrl: 'partials/account-personal.html',
         });
   });
})();
