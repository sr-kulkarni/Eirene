(function () {
  'use strict';

  angular
    .module('eirene', [
      'eirene.routes',
      'eirene.authentication'
    ]);

  angular
    .module('eirene.routes', ['ngRoute']);
})();
