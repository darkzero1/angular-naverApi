var BookApiApp = angular.module('BookApiApp', []);

BookApiApp.controller('BookApiSearch', ['$scope', function ($scope, $http) {
    $http({
        method : "POST",
        url : "/naverBookSearchApi"
    }).then(function success(response){
        $scope.items = response.lists;
        
    }, function error(response){

    })
}]);
