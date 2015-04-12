'use strict';

/* App Module */

var dpiApp = angular.module('dpiApp', [
  'ngRoute',
  'dpiControllers'
]);

dpiApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/table', {
        templateUrl: '/table'
        // ,controller: 'TableCtrl'
      }).
      when('/dpi', {
        templateUrl: '/dpimain'
      }).
      when('/test', {
        templateUrl: '/static/template/test.html'
      }).
      otherwise({
        redirectTo: '/table'
      });
  }]);
