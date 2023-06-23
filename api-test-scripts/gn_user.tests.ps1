Describe "gn_user API Tests" {
    
    # Arrange
    $baseUrl = "http://localhost:31000/"
    
    $headers = @{
        "Content-Type" = "application/json"
    }

    Context "HTTP GET (list) first page of supplier item (for purchase order) with sort - data page of records" {

        # Arrange
        $url = "$($baseUrl)/gn_user"
        
        # Act
        $result = Invoke-RestMethod -Method Get -Uri $url -Headers $headers
Write-Output $result
Write-Host $result

        # Asserts
        It "should have 3 records." {
            # $result.totalRecordCount -gt 0 | Should Be $true
            $result.data.length | Should Be 3
            Write-Output $result.data
Write-Output $result
        }
    }

}