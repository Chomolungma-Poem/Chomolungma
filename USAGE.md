<img src="document/image/icon.svg" width="15px" /> CHOMOLUNGMA

1. #### CML(Chomolungma Markup Language)
    1. ***Structure elements***
       1. *cml*
          - **summary** Root element of CML file
          - **element** *item* ( *N* )
          - **element** *main* ( *N* )
       2. *item*
          - **summary** Items that need to be exported to other code
          - **attribute** *name*
            - **summary** The name of the item used for the call
            - **type** String
          - **attribute** *permission*
            - **summary** How to access this item
            - **type** Enum
              - **value** cannot
                - **summary** Cannot visit
              - **value** readable
                - **summary** Only read
              - **value** writable
                - **summary** Can write
          - **element** ***Value elements*** ( *1* )
       3. *main*
          - **summary** Codes in it will be run
          - **attribute** *name*
            - **summary** The name of the program to be used for calling command line arguments
            - **type** String
            - **example** *test.cml*
            ```xml
            <cml>
                <main name="1+1">
                ...
                </main>
                <main name="1*1">
                ...
                </main>
            </cml>
            ```
            ```shell
            >>> chomolungma build test.cml
            >>> chomolungma run test.cbc 1+1
            2
            >>> chomolungma run test.cbc 1*1
            1
            ```
    2. ***Value elements***
       1. *bit*
          - **summary** Bit string
          - **type** String
            - **type** Enum
              - **value** 0
              - **value** 1
       2. 
        