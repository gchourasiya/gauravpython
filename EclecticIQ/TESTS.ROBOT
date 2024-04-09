*** Settings ***
Library     testDataValidation.TestDataValidation
Library    BuiltIn
Library    Selenium2Library
Resource    ./COMMON-KW.ROBOT

*** Variables ***
${filter}      ${EMPTY}
${column}         name
${noOfCases}    number of cases
${avgImpactScore}   average impact score
${complexity}       complexity
${filterby}     ${filter}
${sortby}       ${column}
${browser}      headlessfirefox
${url}      https://mystifying-beaver-ee03b5.netlify.app/
${table_xpath}      xpath://div[@class='table']
*** Test Cases ***

SORT-BY-NUMBER-OF-CASES
    ${df}       COMMON-KW.CREATE-DATAFRAME
    Log     ${df}

SORT-BY-COLUMN-NAME
#    [Arguments]    ${sortby}
    ${df}       COMMON-KW.CREATE-DATAFRAME
    ${df}       sortByColName       ${df}       ${sortby}
    Log     ${df}


FILTER-ROWS-BY-COLUMN-NAME
#    [Arguments]    ${filterby}
    ${df}       COMMON-KW.CREATE-DATAFRAME
    ${df}       filterData      ${df}       ${sortby}        ${filterby}
    Log     ${df}

SORT-AND-FILTER-DATA
#    [Arguments]    ${sortby}        ${filterby}
    ${df}       COMMON-KW.CREATE-DATAFRAME
    ${df}       filterData      ${df}       ${sortby}        ${filterby}
    ${df}       sortByColName       ${df}       ${sortby}
    Log     ${df}
