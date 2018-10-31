var BookApiApp = angular.module('BookApiApp', []);

BookApiApp.controller('BookApiSearch', ['$scope', function ($scope, $http) {
    $http({
        method : "POST",
        url : "/naverBookSearchApi"
    }).success(function (data, status, headers, config){
        $scope.items = data.lists;
    }).error(function (data, status, headers, config){

    })
}]);
