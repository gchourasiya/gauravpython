*** Settings ***
Library    testDataValidation.TestDataValidation
Library    BuiltIn
Library    Selenium2Library
Library    Collections

*** Variables ***
${browser}      headlessfirefox
${url}      https://mystifying-beaver-ee03b5.netlify.app/
${table_xpath}      xpath://div[@class='table']
${table_header_xpath}       xpath://div[@class='header__item']//a
${table_row_xpath}          xpath://div[@class='table-content']//div[@class='table-row']
*** Keywords ***
GET-TABLE-DATA
    open browser        ${url}      ${browser}
    maximize browser window
    capture page screenshot
    element should be visible       ${table_xpath}
    element should be enabled       ${table_xpath}


    ${headerlen}    Get Element count       ${table_header_xpath}
    Log     ${headerlen}

    @{table_data}=    Create List
    ${table_elements}=    Get WebElements    ${table_xpath}
    FOR    ${element}    IN    @{table_elements}
        ${text}=    Get Text    ${element}
        Log    ${text}
        Append to List      ${table_data}       ${text}
    END
    Log     ${table_data}

    close all browsers
    [Return]        ${headerlen}       ${table_data}

CREATE-DATAFRAME
    ${headerlen}   ${table_data}        get-table-data
    ${df}       convertTodf     ${headerlen}        ${table_data}
    ${df}       regularizeNoOfCasesValues    ${df}
#    ${df}       convert2String      ${df}
    [Return]    ${df}

