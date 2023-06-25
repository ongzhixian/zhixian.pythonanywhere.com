Describe "gn_user API Tests" {
    
    # Arrange
    $baseUrl = "http://localhost:31000/"
    $sharedData = @{}
    
    $headers = @{
        "Content-Type" = "application/json"
    }

    Context "Send valid credentials to get auth-ticket" {

        # Arrange
        $url = "$($baseUrl)api/gn/auth-ticket"
        
        $body = @{
            "username" = "testuser1"
            "password" = "testpassw0rd"
        } | ConvertTo-Json -Compress

        # Act
        try {
            
            $result = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -body $body
            
        } catch {
            Write-Host $_
        }

        # Asserts
        It "should return a JWT string" {
            # $result.totalRecordCount -gt 0 | Should Be $true
            $result.length | Should BeGreaterThan 0
            $sharedData["jwt"] = $result
        }
    }

    # Context "Send a valid auth-ticket JWT for validation" {

    #     # Arrange
    #     $url = "$($baseUrl)api/gn/check-auth-ticket"

    #     $body = @{
    #         "body" = $sharedData["jwt"]
    #     } | ConvertTo-Json -Compress

    #     # Act
    #     try {
    #         $result = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -body $body
    #     } catch {
    #         Write-Error $_
    #     }

    #     # Asserts
    #     It "should return OK." {
    #         $result | Should Be "OK"
    #         # $result.totalRecordCount -gt 0 | Should Be $true
    #         # $result.data.length | Should Be 3
    #         # Write-Output $result.data
    #     }
    # }

    Context "Send a valid auth-ticket JWT to get a refreshed JWT" {

        # Arrange
        $url = "$($baseUrl)api/gn/refresh-auth-ticket"

        $headers = @{
            "Content-Type" = "application/json"
            "Bearer" = $sharedData["jwt"]
        }
        
        # Act
        try {
            $result = Invoke-RestMethod -Method Post -Uri $url -Headers $headers
            Write-Host $result
        } catch {
            Write-Error $_
        }

        # Asserts
        It "should return OK." {
            $result | Should Be "OK"
            # $result.totalRecordCount -gt 0 | Should Be $true
            # $result.data.length | Should Be 3
            # Write-Output $result.data
        }
    }
}