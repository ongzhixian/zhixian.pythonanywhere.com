Describe "gn_user API Tests" {
    
    # Arrange
    $baseUrl = "http://localhost:31000/"
    
    $headers = @{
        "Content-Type" = "application/json"
    }

    Context "HTTP GET (list) first page of supplier item (for purchase order) with sort - data page of records" {

        # Arrange
        $url = "$($baseUrl)api/gn/gn-user"
        
        # Act
        $result = Invoke-RestMethod -Method Get -Uri $url -Headers $headers

        # Asserts
        It "should have 3 records." {
            # $result.totalRecordCount -gt 0 | Should Be $true
            $result.data.length | Should Be 3
            Write-Output $result.data
        }
    }

    Context "Add new user" {

        # Arrange
        $url = "$($baseUrl)api/gn/gn-user"
        
        $body = @{
            "username" = "testuser1"
            "password" = "testpassw0rd"
        } | ConvertTo-Json -Compress

        # Act
        $result = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -body $body

        # Asserts
        It "should have 3 records." {
            # $result.totalRecordCount -gt 0 | Should Be $true
            $result.data.length | Should Be 3
            Write-Output $result.data
        }
    }
}