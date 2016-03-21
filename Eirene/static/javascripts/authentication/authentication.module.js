(function () {
  'use strict';

  angular
    .module('eirene.authentication', [
      'eirene.authentication.controllers',
      'eirene.authentication.services'
    ]);

  angular
    .module('eirene.authentication.controllers', []);

  angular
    .module('eirene.authentication.services', ['ngCookies']);
})();
