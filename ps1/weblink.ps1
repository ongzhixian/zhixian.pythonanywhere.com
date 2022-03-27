# Invoke-Pester -TestName "/api/common/utc"

$base_url = "http://localhost:31000"

Describe "/api/weblink" -Tags "unit" {
    
    $headers = @{
        "Content-Type" = "application/json"
    }

    Context "When posting no content" {
        It "should throw bad request" {
            { 
                Invoke-RestMethod -Method Post -Uri "$base_url/api/weblink" -headers $headers 
            } | Should Throw "BAD REQUEST"
        }
    }

    Context "When posting a list links using Invoke-WebRequest" {
        $body = @(
            "link1", "link2", "link3"
        ) | ConvertTo-Json

        $response = Invoke-WebRequest -Method Post -Uri "$base_url/api/weblink" -headers $headers -body $body

        It "should return a response of type BasicHtmlWebResponseObject" {
            $response | Should BeOfType Microsoft.PowerShell.Commands.BasicHtmlWebResponseObject
            
        }

        It "should return a HTTP 201 (created)" {
            $response.StatusCode | Should Be 201
        }

        It "should return content of '3 links processed'" {
            $response.Content | Should Be "3 links processed"
        }
    }

    # This example shows why Invoke-RestMethod is probably not a good choice for testing API
    # Main reason: The response object is a string/PsCustomObject instead of WebResponse object
    #              So we cannot test HTTP status code.
    # Context "When posting a list links using Invoke-RestMethod" {
    #     $body = @(
    #         "link1", "link2", "link3"
    #     ) | ConvertTo-Json
    #     $response = Invoke-RestMethod -Method Post -Uri "$base_url/api/weblink" -headers $headers -body $body
    #     It "should return a response of type string" {
    #         $response | Should BeOfType System.String
    #     }
    #     It "should be string 'OKOK'" {
    #         $response | Should Be "OKOK"
    #     }
    # }


    # Context "When HTTP GET /" {

    #     It "default (no parameters)" {
    #         # Arrange
    #         $body = @{
    #             "arg1" = "arg1 content";
    #             "arg2" = "arg2 content";
    #         } | ConvertTo-Json
    #         $body = @(
    #             "link1", "link2", "link3"
    #         )
                

    #         # Act
    #         #$res = Invoke-WebRequest $url -Method Get -Headers $headers
    #         $a = Invoke-RestMethod -Method Post -Uri "$base_url/api/weblink" -headers $headers -body $body
    #         Write-Host $a
    #         # Write-Host $a.name
    #         # Write-Host $a.GetType().ToString()
              # Wait-Debugger
            
    #         # Asserts
    #         $true | Should Be $true
    #         # $a.name | Should Be /api/common/utc
    #     }
    # }

}