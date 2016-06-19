(function(){
   var app = angular.module('moneyviz', ['ui.router', 'ngAnimate']);

   app.factory('d3', function() { return d3; });

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
         .state('account', {
            url: '/',
            templateUrl: 'partials/account.html',
         })
         .state('account-settings', {
            url: '/',
            templateUrl: 'partials/account-settings.html',
         });
   });

   app.controller('UploadController', ['d3', 'TransactionService', function(d3, ts) {
      var csvAsDataURL;
      var fileinput = document.getElementById('uploadFileInput');

      this.logTransactions = function() {
         console.log(ts.getTransactions());
      };

      fileinput.addEventListener('change', function(e) {
         var reader = new FileReader();
         reader.addEventListener('loadend', function(e) {
            csvAsDataURL = e.target.result;
            processCSV(csvAsDataURL);
         });
         reader.readAsDataURL(e.target.files[0]);
      });

      function processCSV(dataURL) {
         d3.csv(dataURL, function(dataset) {
            ts.addBulkTransactions(dataset);
         });
      };
   }]);

   app.factory('TransactionService', ['$http', function($http) {
      var transactions = [];
      function normalizeTransactions(trans) {
         return trans.map(function(currentValue) {
            // Lowercase all of the keys for the API e.g. date not Date
            var key, keys = Object.keys(currentValue);
            var n = keys.length;
            var newObj = {};
            while(n--) {
               key = keys[n];
               newObj[key.toLowerCase()] = currentValue[key];
            }
            return newObj;
         });
      }

      return {
         addBulkTransactions: function(trans) {
            transactions = transactions.concat(trans);
            console.log("Storing " + transactions.length + " transactions");
            $http({
               method: 'PATCH',
               url: '/api/v1/transactions',
               headers: {
                  'Authorization': 'ApiKey karl:e1f8bf1257b600b8f5c8caa0719fed087c998bb8'
               },
               data: {
                  'objects': normalizeTransactions(trans)
               }
            }).then(function successCallback(response) {
               console.log("Success: " + response);
            }, function errorCallback(response) {
               console.log("Error: " + response);
            });
         },
         getTransactions: function() {
            return transactions;
         }
      };
   }]);
})();
