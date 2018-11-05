var BookApiApp = angular.module('BookApiApp', []);

BookApiApp.controller('BookApiSearch', ['$scope', '$http', function ($scope, $http) {
    $scope.search_name ="";

    $scope.searchBook = function(){
      var jsonData = {"search_name" : $scope.search_name}
      $http({
            method : "POST",
            url : "/naversearch/",
            headers :{'X-CSRFToken' : document.getElementsByName('csrfmiddlewaretoken')[0].value,
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'},
            data : $.param(jsonData)
        }).then(function (response){
            $scope.items = response.data.items;

          }, function (error){

        })
      }

}]);

BookApiApp.filter('changeHtml',['$sce', function($sce) {
      return function(text) {
        return $sce.trustAsHtml(text);
      };
  }]);
