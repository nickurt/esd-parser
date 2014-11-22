## Electronic Software Download (ESD) Parser
### Works with
* Windows 8.1
* Windows 10

### Example
#### Convert ESD to Buildstring
    # Windows 8.1 based
    run.py 9600.17053.winblue_refresh.140923-1144_x86fre_client_professional_en-us-ir4_cpra_x86frer_en-us_esd.esd

    # Returns ...
    // 6.3.9600.17053 (winblue_refresh.140923-1144)
    - - - 
    # Windows 10 based
    run.py 9836.0.140906-2314.fbl_release_CLIENTENTERPRISE_VOL_x64fre_en-us.esd
    // 6.4.9836.0 (fbl_release.140906-2314)
	
    run.py 9888.0.141113-2137.fbl_release_CLIENTPRO_RET_x64fre_en-us.esd
    // 10.0.9888.0 (fbl_release.141113-2137)