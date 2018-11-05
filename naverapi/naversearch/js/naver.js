var BookApiApp = angular.module('BookApiApp', []);

BookApiApp.controller('BookApiSearch',  function ($scope, $http) {
    $scope.search_name ="";
    $scope.searchBook = function(){
        $http({
            method : "POST",
            url : "/naverapi"
            data : {"search_name" : $scope.search_name}
        }).success(function (data, status, headers, config){
            $scope.items = data.lists;
        }).error(function (data, status, headers, config){

        })
    }

});
