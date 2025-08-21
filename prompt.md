
        You are a parser. Output JSON only. No explanations.
        If you cannot find a value, return an empty string.

        REQUIRED OUTPUT FORMAT:
        ```json
        {
          "selectors": {
            "title": "",
            "description": "",
            "company": "",
            "company_url": "",
            "posted_date": ""
          }
        }
        ```

        EXAMPLE OUTPUT:
        ```json
        {
          "selectors": {
            "title": "h1.job-title",
            "description": "div.job-description",
            "company": ".company-name",
            "company_url": "a.company-name",
            "posted_date": ".posted-date"
          }
        }
        ```

        Analyze the provided HTML content from a job detail page and infer the CSS selectors for the following fields:
        - `title`: The job title or position name.
        - `description`: The full job description content.
        - `company`: The company name.
        - `company_url`: The URL of the company.
        - `posted_date`: The date the job was posted.

        If a field is not found or not applicable, use an empty string for its value.
        
            The content provided is HTML from a job detail page. Carefully analyze this HTML content.
            Infer the most accurate CSS selectors for the following job detail fields:
            - `title`: The job title or position name.
            - `description`: The full job description content.
            - `company`: The company name.
            - `company_url`: The URL of the company.
            - `posted_date`: The date the job was posted.

            HTML Content:
            ```html
            <html class=" chrome  psc_dir-ltr psc_form-medium" dir="ltr" lang="en"><!-- Copyright (c) 2000, 2022, Oracle and/or its affiliates.  --><head>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width,user-scalable=yes,initial-scale=1.0,minimum-scale=1.0">
<script language="JavaScript">
var  totalTimeoutMilliseconds = 2073600000; 
var  warningTimeoutMilliseconds = 2073600000; 
var timeOutURL = 'https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/?cmd=expire';
var timeoutWarningPageURL = 'https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/s/WEBLIB_TIMEOUT.PT_TIMEOUTWARNING.FieldFormula.IScript_TIMEOUTWARNING';
var sRCRequestURL = 'https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/s/WEBLIB_PTRC.ISCRIPT1.FieldFormula.IScript_RC_REQUEST';
</script> 

<link rel="apple-touch-icon" href="/cs/hcm/cache/pdhcm_250316/LOGO_FAVICON_1.png">
<link rel="icon" href="/cs/hcm/cache/pdhcm_250316/LOGO_FAVICON_1.png">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/PSSTYLEDEF_FMODE_1.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/HRS_CG_SS_9.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/HRS_CG_SEARCH_SS_9.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/PTS_INTELLISCHCSS_1.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/PTNUI_NAVBAR_CSS_1.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/CC_HRS_CG_GUEST_SS_1.css">
<link rel="stylesheet" type="text/css" href="/cs/hcm/cache/pdhcm_250316/CC_DEFAULT_FLUID_SS_8.css" ptbranding="true">
<title>Careers</title>
<script language="JavaScript">
try {
document.domain = "calgary.ca";
}
catch(err) {;}
</script>
<script language="JavaScript">
var winName='win0';
var winParent = null;
var modalID = null;
var modalZoomName = null;
var baseKey_win0 = "\x1b\r\n";
var altKey_win0 = "0J5678\xbc\xbe\xbf\xde";
var ctrlKey_win0 = "JK";
var saveWarningKeys_win0 = "";
var firstFocusID = null;
var bPTDrag = false;
var sMDWrapperStyle='', sMDSide1Style='', sMDSide2Style='', sMDHeaderStyle='', sMDFooterStyle='', sPageFFStyle='';
var refererURL = 'https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?FOCUS=Applicant&Page=HRS_APP_JBPST_FL&JobOpeningId=312471&PostingSeq=1&SiteId=1&';
var isNewSaveWarn = true;
var bAccessibility_win0 =false;
var bFMode =true;
var bDoModal_win0 = false;
var bJSModal_win0 = false;
var bPromptPage_win0 = false;
var bTabOverTB_win0 = false;
var bTabOverPg_win0 = false;
var bTabOverNonPS_win0 = false;
var strCurrUrl='https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?FOCUS=Applicant&Page=HRS_APP_JBPST_FL&JobOpeningId=312471&PostingSeq=1&SiteId=1&&PAGE=HRS_APP_JBPST_FL';
var strReqURL='';
var bIncInNavigation='T';
var szPinCrefID='HC_HRS_CG_SEARCH_FL_GBL2';
var szPinCrefReg='T';
var szPinCrefLabel='Careers';
var szCrefID='HC_HRS_CG_SEARCH_FL_GBL2';
var szCrefReged='T';
var szCrefVisible='T';
var szCrefLabel='Careers';
var szCrefQS='FOCUS=Applicant';
var szCrefUsageType='TARG';
var localNodes = ['HRMS', 'PSFT_HR'];
var remoteUrls = ['https://myhrconnect.calgary.ca/psp/myhr/EMPLOYEE/EHR', 'https://fscm.alt.calgary.ca/psp/fscm/EMPLOYEE/ERP'];
bGenDomInfo = false;
var szCalendarType = 'G';
var bMenuSrchPage = false;
var bGuidedAG = false;
var bWSRP=0;var szMenuSrchText = "-999999-";
var disablePNSubscriptions=0;var modalBackUrl = '/cs/hcm/cache/pdhcm_250316/PT_NUI_BACK_SMALL_IMG_1.svg';
var modalBackAlt = 'Back';
var sPopupTitle = 'Popup window';
var modalCloseUrl = '/cs/hcm/cache/pdhcm_250316/PT_MODAL_CLOSE_NUI_1.svg';
var modalCloseAlt = 'Close';
var modalResizeUrl= '/cs/hcm/cache/pdhcm_250316/PT_RESIZE_IMG_1.svg';
var modalResizeAlt = 'Drag to resize';
var modalMoveAlt = 'Drag to move';
</script>
<script language="JavaScript">
bPTActEnterKey = true;
</script>
<script language="JavaScript">
var scrollFieldListOld = [['win0hdrdivPT_ACTION_MENUgrp',1, 0, 0, 0,0, 1,0,0, 1],['win0hdrdivPT_CONTEXT_MENUgrp',1, 0, 0, 0,0, 1,0,0, 1]];var scrollFieldList = [['win0hdrdivPT_ACTION_MENUgrp',1, 0, 0, 0,0, 1,0,0, 1],['win0hdrdivPT_CONTEXT_MENUgrp',1, 0, 0, 0,0, 1,0,0, 1]];
</script>
<script language="JavaScript">
var agGroupletList = [];var groupletList = [];groupletList = [['win0divPTLAYOUT_PT_MENU_PRESENT','15','','','0','bGrouplet@1;','','0','','','','0','']];
</script>
<script language="JavaScript">
try {
document.domain = "calgary.ca";
}
catch(err) {;}
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_COMMON_FMODE_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_AJAX_NET_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_SAVEWARNINGSCRIPT_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_PAGESCRIPT_win0_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_EDITSCRIPT_win0_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PT_PAGESCRIPT_FMODE_MIN_1.js">
</script>
<script language="JavaScript">
DoUrlNUI();
var nResubmit=0;
var nLastAction=0;
var loader=null;
if (typeof(bCleanHtml) == 'undefined')
	var bCleanHtml = false;
setupTimeout2();
var postUrl_win0='https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL';
function aAction_win0(form, id, params, bAjax, bPrompt, sAjaxTrfUrl, bWarning, sScriptAfter, nTrfURLType)
{
setupTimeout2();
if ((id != '#ICSave'))
processing_win0(1,3000);
aAction0_win0(form, id, params, bAjax, bPrompt, sAjaxTrfUrl, bWarning, sScriptAfter, nTrfURLType);
}
function submitAction_win0(form, id, event, sAjaxTrfUrl, bWarning, sScriptAfter, nTrfURLType)
{
setupTimeout2();
if (!ptCommonObj2.isICQryDownload(form, id))
 { processing_win0(1,3000); }
preSubmitProcess_win0(form, id);
var spellcheckpos = id.indexOf('$spellcheck');
if ((spellcheckpos != -1) && (id.indexOf('#KEYA5') != -1))
	form.ICAction.value = id.substring(0,spellcheckpos);
else 
	form.ICAction.value=id;
var actionName = form.ICAction.value;
form.ICXPos.value=ptCommonObj2.getScrollX();
form.ICYPos.value=ptCommonObj2.getScrollY();
bcUpdater.storeBcDomData();
if ((typeof(bAutoSave) != 'undefined') && bAutoSave)
	form.ICAutoSave.value = '1';
if (!ptCommonObj2.isAJAXReq(form, id) && !ptCommonObj2.isPromptReq(id)){
if (nLastAction == 1 && nResubmit > 0) return;
form.ICResubmit.value=nResubmit;
form.submit();
if (!ptCommonObj2.isICQryDownload(form, id))
	nResubmit++;
}
else if (ptCommonObj2.isPromptReq(id))
	pAction_win0(form, id, arguments[2]);
else
	aAction_win0(form, actionName, null, true, false, sAjaxTrfUrl, bWarning, sScriptAfter, nTrfURLType);
cancelBubble(event);
}
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PTMAF_PUSH_JS_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/PTS_INTELLISEARCH_JS_win0_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/CC_HR_HIDEHDRELEM_JS_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/CC_TRPS_JS_MIN_1.js">
</script>
<script language="JavaScript" type="text/javascript" src="/cs/hcm/cache/pdhcm_250316/CC_EXT_COMPANYINFO_CITY_LOGO_MIN_233780.js">
</script>
<script language="javascript">
var pt_calHeadstyle=" class='PTCALHEAD' "
var pt_calWeekHeadstyle=" class='PTCALWEEKHEAD' "
function dateitemrefs()
{
this.pt_dateheader = "/cs/hcm/cache/pdhcm_250316/PT_PORTAL_IC_CLOSE_SD_CSS_1.gif";
this.pt_datering = "/cs/hcm/cache/pdhcm_250316/PT_CURRENT_DATE_SD_CSS_1.gif";
this.pt_datesel = "/cs/hcm/cache/pdhcm_250316/PT_SELECTED_DATE_SD_CSS_1.gif";
this.pt_nextmonth = "/cs/hcm/cache/pdhcm_250316/PT_RIGHT_SCROLL_SD_CSS_1.gif";
this.pt_prevmonth= "/cs/hcm/cache/pdhcm_250316/PT_LEFT_SCROLL_SD_CSS_1.gif";
this.pt_daystitle_hijri = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_S6_1.GIF";
this.pt_daystitle_thai = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_S0_1.GIF";
this.pt_daystitle_s0 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_S0_1.GIF";
this.pt_daystitle_m1 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_M1_1.GIF";
this.pt_daystitle_t2 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_T2_1.GIF";
this.pt_daystitle_w3 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_W3_1.GIF";
this.pt_daystitle_t4 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_T4_1.GIF";
this.pt_daystitle_f5 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_F5_1.gif";
this.pt_daystitle_s6 = "/cs/hcm/cache/pdhcm_250316/PT_DATE_TITLE_S6_1.GIF";
}
 
function LoadCalendar()
{
var dateitems = new dateitemrefs();
loadImages(dateitems);
}
function DatePrompt0_win0(dtfield,promptfield,yrfmt,bsubmit)
{
setupTimeout2();
openDate_win0(dtfield, promptfield, "DMY/"+yrfmt,bsubmit,"G",0);
}
</script>
<script language="JavaScript" ptdefer="defer">
var bInModal = false;
function onLoadExt_win0() {
modalZoomName = null;
initWorkers('/cs/hcm/cache/pdhcm_250316/PT_WORKER_MIN_1.js',5);

 g_bAccessibilityMode=false;
var actn='';
setKeyEventHandler_win0();setMouseEventHandler();
ptEvent.add(window,'scroll',positionWAIT_win0);
if (typeof(ptLongEditCounter) != 'undefined' && ptLongEditCounter != null)
   ptLongEditCounter.onLoadLongEditCounter();
objToBeFocus = null;
if (bPTDrag) CancelDragAccessible();
 bPTDrag = false;
if (typeof oWin == 'undefined') setEventHandlers_win0('ICFirstAnchor_win0', 'ICLastAnchor_win0', false);
 else
 oWin.setEventHandlers_win0('ICFirstAnchor_win0', 'ICLastAnchor_win0', false);
try{
ptsSearchUIObj.initSearch("{\"page\":\"HRS_APP_JBPST_FL\",\"placeholder\":\"\",\"searchcategory\":\"\",\"scLabel\":\"\",\"includeHiddenCref\":false,\"includeOnlyCompOrGeneric\":false,\"showGridIcons\":true,\"showCategoryDropDown\":true,\"showGlobalSearchButton\":true,\"componentSearchURL\":\"\",\"hideSearch\":true,\"openSearchInModal\":false,\"isInitialLoad\":false,\"showCompletePath\":false,\"keywordLabel\":\"\",\"srchWidgetId\":\"win0hdrdivPTS_SEARCHWIDGET\",\"isAccessibilityMode\":false}")
portalContextNodeURI = 'https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS';
SearchPageClose();
var BrandRTEValue = PTRTEFillcache('https://recruiting.calgary.ca/psp/hcm_newwin/EMPLOYEE/HRMS/c/PTGP_MENU.PTGP_USERPREF_FL.GBL','PT_RTE_IMG_DB_LOC','record://PTRTDB','PT_BRAND_COMPINFO','1');var BrandAreaObject = document.getElementById('PT_BRAND_COMPINFO');if (typeof(BrandAreaObject) != 'undefined' && BrandAreaObject != null) BrandAreaObject.innerHTML = BrandRTEValue;
ChangeCityLogoExt('PD','PDHCM')
var RichTextValue = PTRTEFillcache('/psc/hcm_newwin/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL','PT_RTE_IMG_DB_LOC','record://PTRTDB','HRS_SCH_PSTDSC_DESCRLONG$0','1');
var TextAreaObject = document.getElementById('HRS_SCH_PSTDSC_DESCRLONG$0');
if (typeof(TextAreaObject) != 'undefined' && TextAreaObject != null) TextAreaObject.innerHTML = RichTextValue;

var RichTextValue = PTRTEFillcache('/psc/hcm_newwin/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL','PT_RTE_IMG_DB_LOC','record://PTRTDB','HRS_SCH_PSTDSC_DESCRLONG$1','1');
var TextAreaObject = document.getElementById('HRS_SCH_PSTDSC_DESCRLONG$1');
if (typeof(TextAreaObject) != 'undefined' && TextAreaObject != null) TextAreaObject.innerHTML = RichTextValue;

var RichTextValue = PTRTEFillcache('/psc/hcm_newwin/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL','PT_RTE_IMG_DB_LOC','record://PTRTDB','HRS_SCH_PSTDSC_DESCRLONG$2','1');
var TextAreaObject = document.getElementById('HRS_SCH_PSTDSC_DESCRLONG$2');
if (typeof(TextAreaObject) != 'undefined' && TextAreaObject != null) TextAreaObject.innerHTML = RichTextValue;

var RichTextValue = PTRTEFillcache('/psc/hcm_newwin/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL','PT_RTE_IMG_DB_LOC','record://PTRTDB','HRS_SCH_PSTDSC_DESCRLONG$3','1');
var TextAreaObject = document.getElementById('HRS_SCH_PSTDSC_DESCRLONG$3');
if (typeof(TextAreaObject) != 'undefined' && TextAreaObject != null) TextAreaObject.innerHTML = RichTextValue;

}catch(e) { if(typeof String !== 'undefined') alert('custom javascript error ' + e.message); }
if (top.window.isFModeLayout() && (typeof top.window.initHelp == 'function')) top.window.initHelp();
postUrl_win0='https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL';
if (typeof(initScrolls0) != 'undefined' && initScrolls0 != null) initScrolls0(false);
setFocus_win0('HRS_SCH_WRK_HRS_SCH_TEXT100',-1);
loadGrouplets('/cs/hcm/cache/pdhcm_250316/PT_WORKER_MIN_1.js',5);
ptLoadingStatus_empty(0);
setupTimeout2();
processing_win0(0,3000);
ptConsole2.enable();
}
try{ptEvent.load(onLoadExt_win0);}catch(e){}
</script></head>
<body tabindex="-1">
<div id="pt_envinfo" devicetype="" browser="CHROME/139.0/WIN"></div>
<form id="HRS_CG_SEARCH_FL" name="win0" method="post" action="https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL" autocomplete="off" class="PSForm">
<div class="ps_box-toolshiddens" id="win0divPSTOOLSHIDDENS"><div class="ps_modalmask_cover psc_hidden" id="pt_modalMaskCover">&nbsp;</div><div class="ps_modalmask psc_hidden" id="pt_modalMask">&nbsp;</div><div id="pt_modals" class="ps_modal_controller"><div id="ptModalShadow" class="popupDragFrame" style="cursor:nw-resize">&nbsp;</div></div>
<div class="ps_ajax_console psc_hidden" id="pt_console"><input type="button" id="COPYCONSOLE" value="Copy" onclick="ptConsole2.copy();" alt="copy to clipboard" title="copy to clipboard"><input type="button" id="CLEARCONSOLE" onclick="ptConsole2.clear();" value="Clear" alt="clear console" title="clear console"><input type="button" id="HIDECONSOLE" onclick="ptConsole2.hide();" value="Hide" alt="hide console" title="hide console"><input type="button" id="CLOSECONSOLE" onclick="ptConsole2.deactive();" value="Close" alt="close console" title="close console"></div><div class="ps_box-group psc_layout psc_skipnav_container" id="PT_SKIPNAV_CONT">
<div class="ps_box-link psc_skipnav"><span class="ps-link-wrapper"><a class="ps-link" id="PT_SKIPNAV" onclick="javascript:cancelBubble(event);" href="javascript:SetMainContentFocus();" onblur="javascript:SetMainContentFocus(false);">Skip to Main Content</a></span></div>
</div>
<div class="ps_typeahead psc_hidden" id="pt_typeahead0"><div id="pt_typeahead" class="ps_box-typeahead">&nbsp;</div></div><div class="ps_box-announce ps_alert-normal" aria-live="polite" id="pt_liveregion"></div>
<div id="pt_dnd_win0" class="psc_hidden-readable">Press Control+M to start dragging object</div>
<div class="psc_processing psc_hidden" id="WAIT_win0" style="visibility: hidden; display: none;"><img id="processing" src="/cs/hcm/cache/pdhcm_250316/PT_PROCESSING_FMODE_1.gif" alt="Processing... please wait" title="Processing... please wait"></div>
 <div style="visibility:hidden; display:none; position:absolute;left:auto;top:-10000px; width:1px; height:1px;overflow:hidden;" aria-relevant="text additions" aria-live="assertive" aria-atomic="true" class="psc_processing psc_hidden" id="Delayed_win0">&nbsp;</div><div class="psc_saved psc_hidden" id="SAVED_win0" style="visibility: hidden; display: none;"><div><div id="saveWait_win0"><img src="/cs/hcm/cache/pdhcm_250316/PT_LOADER_1.gif" width="24" height="24" alt=""></div><div class="ps_saved_text"><span id="ptStatusText_win0">&nbsp;</span></div></div></div><div class="x" id="win0divPSHIDDENFIELDS" style="display:none"><input type="hidden" name="ICType" id="ICType" value="Panel">
<input type="hidden" name="ICElementNum" id="ICElementNum" value="0">
<input type="hidden" name="ICStateNum" id="ICStateNum" value="2">
<input type="hidden" name="ICAction" id="ICAction" value="None">
<input type="hidden" name="ICModelCancel" id="ICModelCancel" value="0">
<input type="hidden" name="ICXPos" id="ICXPos" value="0">
<input type="hidden" name="ICYPos" id="ICYPos" value="0">
<input type="hidden" name="ResponsetoDiffFrame" id="ResponsetoDiffFrame" value="-1">
<input type="hidden" name="TargetFrameName" id="TargetFrameName" value="None">
<input type="hidden" name="FacetPath" id="FacetPath" value="None">
<input type="hidden" name="ICFocus" id="ICFocus" value="">
<input type="hidden" name="ICSaveWarningFilter" id="ICSaveWarningFilter" value="0">
<input type="hidden" name="ICChanged" id="ICChanged" value="0">
<input type="hidden" name="ICSkipPending" id="ICSkipPending" value="0">
<input type="hidden" name="ICAutoSave" id="ICAutoSave" value="0">
<input type="hidden" name="ICResubmit" id="ICResubmit" value="0">
<input type="hidden" name="ICSID" id="ICSID" value="iQpmmLJAF2Pg7PgFyiqERWUjySE7eSdQYqhDE8My7Ns=">
<input type="hidden" name="ICActionPrompt" id="ICActionPrompt" value="false">
<input type="hidden" name="ICBcDomData" id="ICBcDomData" value="">
<input type="hidden" name="ICDNDSrc" id="ICDNDSrc" value="">
<input type="hidden" name="ICPanelHelpUrl" id="ICPanelHelpUrl" value="">
<input type="hidden" name="ICPanelName" id="ICPanelName" value="">
<input type="hidden" name="ICPanelControlStyle" id="ICPanelControlStyle" value="">
<input type="hidden" name="ICFind" id="ICFind" value="">
<input type="hidden" name="ICAddCount" id="ICAddCount" value="">
<input type="hidden" name="ICAppClsData" id="ICAppClsData" value="">
</div>
</div>
<a class="ps-anchor" id="ICFirstAnchor_win0"></a>
<div id="PT_WRAPPER" class="ps_wrapper">
<div class="ps_header" id="PT_HEADER">
<div class="ps_header_panel" id="PT_HEADER_PANEL">
<div class="ps_pspagecontainer_hdr" id="win0divPSPAGECONTAINER_HDR">
<div class="ps_box-group psc_layout ps_header_bar-container" id="win0hdrdivPTLAYOUT_HEADER_GROUPBOX0"><div class=" psc_force-hidden" id="win0hdrdivICSCRIPTSID"><div class="ps_box-label" id="win0hdrdivICSCRIPTSIDlbl"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="ICSCRIPTSID">ptnbsid=NGemVFGlUV7uwRnI3gog8SmLAQQ%3d&amp;ptpinrand=k50lp1cY3SutYv%2fKBdxVzA%3d%3d&amp;ptpinhash=%7b3%7dzv6ntUkpsf9fbfpjyrCY0JF3QXGiVzCH9iI11WpT9aw%3d</span>
</div><div role="region" aria-label="Site Banner" class=" ps_box-headerbranding" id="win0hdrdivPT_BRAND_COMPINFO" style="text-align: center;background-color:white;"><div class="ps_box-label" id="win0hdrdivPT_BRAND_COMPINFOlbl"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="PT_BRAND_COMPINFO">
<span style="color:#f39c12;"><span style="font-size:18px;"><strong><img id="COC_EXTERNAL_LOGO" src="/cs/hcm/cache/pdhcm_250316/COC_EXTERNAL_LOGO_269977.svg" height="65" border="0"></strong></span></span></span>
</div><div role="banner" class=" ps_header_bar" id="win0hdrdivPTLAYOUT_HEADER_GROUPBOX1"><div class=" ps_header_bar_cont" id="win0hdrdivHEADER_BAR_CONT"><div class=" ps_back_cont" id="win0hdrdivPT_NAV_CONT"><div class=" ps_system_cont" id="win0hdrdivPTLAYOUT_HEADER_GROUPBOX4"><div class="ps_box-button psc_toolaction-back psc_header-all   psc_image_only ps_header_button psc_disabled" id="win0hdrdivPT_WORK_PT_BUTTON_BACK"><span class="ps-button-wrapper" title="Back"><a id="PT_WORK_PT_BUTTON_BACK" class="ps-button" role="button" href="javascript:DoBack('win0')" onclick="javascript:cancelBubble(event);"><img src="/cs/hcm/cache/pdhcm_250316/PT_NUI_BACK_PRIM_IMG_1.svg" id="PT_WORK_PT_BUTTON_BACK$IMG" class="ps-img" alt=""><span class="ps-text">Back</span></a></span></div><div class="ps_box-group psc_layout" id="win0hdrdiv$ICField69"></div></div><div class=" ps_custom_cont ps_target-custleft" id="win0hdrdivPT_CUSTOM_LEFT"></div></div><div class=" ps_pagetitle_cont" id="win0hdrdivPT_TITLE_CONT"><div class=" ps_system_cont  ps_target-title  psc_force-hidden" id="win0hdrdivPT_PAGETITLE"><h1 id="PT_PAGETITLE" class="ps_pagetitle"><span class="ps-text" id="PT_PAGETITLElbl">Job Description</span></h1></div><div class=" ps_custom_cont ps_target-custmiddle" id="win0hdrdivPT_CUSTOM_MIDDLE"></div><div class=" ps_headersearch_cont psc_search-subdued" id="win0hdrdivPT_HDR_SEARCH_CONT"><div class="ps_box-group psc_layout pts_search_widget pts_search_widget_hide" id="win0hdrdivPTS_SEARCHWIDGET"><div class="ps_box-group psc_layout pts_search_mask psc_hidden" id="win0hdrdivPTS_MASK"></div><div id="win0hdrdivPORTALOBJ" class=" psc_hidden"><div id="win0hdrdivPORTALOBJlbl" class="ps_box-label"><label for="PORTALOBJ" id="PORTALOBJ_LBL" class="ps-label">&nbsp;</label></div><div id="win0hdrdivPORTALOBJctrl" class="ps_box-control"><input type="text" id="PORTALOBJ" class="ps-edit" value="" maxlength="30" onclick="javascript:cancelBubble(event);">
</div></div><div class="ps_box-group psc_layout pts_search_content psc_hidden" id="win0hdrdivPTSCONTENTBOX"><div class="ps_box-group psc_layout pts_search_controls" id="win0hdrdivPTS_SEARCHEDIT"><div class=" pts_back_button" id="win0hdrdivPTSBACKBTN"><span class="ps-button-wrapper" title="Back"><a id="PTSBACKBTN" class="ps-button" role="button" href="javascript:void(0);'" onclick="javascript:ptsSearchUIObj.ptsCloseAllLists()"><img src="/cs/hcm/cache/pdhcm_250316/PTS_INTSRCH6_ICN_1.svg" id="PTSBACKBTN$IMG" class="ps-img" alt="Back"></a></span></div><div class=" pts_category_button" id="win0hdrdivPTSCATEGORYBTN"><span id="PTSCATEGORYBTN$span" class="ps-button-wrapper"><a id="PTSCATEGORYBTN" class="ps-button" role="button" aria-haspopup="true" ptlinktgt="pt_peoplecode" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSCATEGORYBTN');">Search Category Name</a></span></div><div id="win0hdrdivPTSKEYWORD" class="ps_box-edit pts_editbox psc_label-hidereadable"><div id="win0hdrdivPTSKEYWORDlbl" class="ps_box-label"><label for="PTSKEYWORD" id="PTSKEYWORD_LBL" class="ps-label">Search keywords</label></div><div id="win0hdrdivPTSKEYWORDctrl" class="ps_box-control"><input type="search" id="PTSKEYWORD" class="ps-edit" value="" onclick="javascript:cancelBubble(event);">
</div></div><div class=" pts_search_button" id="win0hdrdivPTSSEARCHBTN"><span class="ps-button-wrapper" title="Search"><a id="PTSSEARCHBTN" class="ps-button" role="button" href="javascript:void(0);" onclick="javascript:ptsSearchUIObj.ptsDoGlobalSearch(this)"><img src="/cs/hcm/cache/pdhcm_250316/PTS_INTSRCH3_ICN_1.svg" id="PTSSEARCHBTN$IMG" class="ps-img" alt="Search"></a></span></div></div><div class="ps_box-group psc_layout pts_category_dropdown psc_hidden ps_scrollable sbar sbar_v ps_scrollable_v" id="win0hdrdivPTSCATEGORIES"><div class="ps_box-group psc_layout psc_width-100pct" id="win0hdrdiv$ICField1"><div class="ps_box-group psc_width-100pct pts_category_header1" id="win0hdrdivPTSCATEGORYHDR"><h2 class="ps_header-group"><span class="ps-text" id="PTSCATEGORYHDRlbl">Search in...</span></h2>
<div class="ps_content-group" id="win0hdrdivPTSCATEGORYHDRgrp">
<div role="presentation" class="ps_box-grid-menu" id="win0hdrdivPTS_INTSCHM_DVW$0"><div role="presentation" class="ps_box-gridc" id="win0hdrdivPTS_INTSCHM_DVWgridc$0"><div role="presentation" class="ps_box-gridc-right" id="win0hdrdivPTS_INTSCHM_DVWgridc-right$0"><div role="presentation" class="ps_box-grid" id="win0hdrdivPTS_INTSCHM_DVW$grid$0"><div class="ps_grid-menu" role="presentation"><ul class="ps_grid-body ps_box-menucontainer ps_menucontainer pt_keynav-list" role="menu"><li class="ps_grid-row ps_box-menuitem" id="PTS_INTSCHM_DVW$0_row_0" role="presentation">
<div role="presentation" class="ps_box-link" id="win0hdrdivPTSMENU$0"><span id="PTSMENU$span$0" class="ps-link-wrapper" role="presentation"><a id="PTSMENU$0" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSMENU$0');">Search Category Name</a></span></div></li></ul></div>
</div></div></div></div></div></div></div></div><div class="ps_box-group psc_layout pts_search_tray psc_hidden ps_scrollable sbar sbar_v ps_scrollable_v" id="win0hdrdivPTSSEARCHTRAY"><div class="ps_box-group psc_layout psc_padding-left5px pts_message psc_hidden" id="win0hdrdivPTSDISPLAYMSG"><div class="ps_box-text" id="win0hdrdiv$ICField45"><span class="ps-text">No results to display</span>
</div></div><div class="ps_box-group psc_layout pts_results_grid" id="win0hdrdivPTSRESULTS"><div role="presentation" class="ps_box-grid-menu psc_width-100pct psc_grid-norowcount" id="win0hdrdivPTS_INTELLISRCH_RS$0"><div role="presentation" class="ps_box-gridc" id="win0hdrdivPTS_INTELLISRCH_RSgridc$0"><div role="presentation" class="ps_box-gridc-right" id="win0hdrdivPTS_INTELLISRCH_RSgridc-right$0"><div role="presentation" class="ps_box-grid" id="win0hdrdivPTS_INTELLISRCH_RS$grid$0"><div class="ps_grid-menu" role="presentation"><ul class="ps_grid-body ps_box-menucontainer ps_menucontainer pt_keynav-list" role="menu"><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_0" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$0"><span id="PTSTITLE$span$0" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$0" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$0');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_1" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$1"><span id="PTSTITLE$span$1" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$1" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$1');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_2" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$2"><span id="PTSTITLE$span$2" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$2" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$2');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_3" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$3"><span id="PTSTITLE$span$3" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$3" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$3');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_4" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$4"><span id="PTSTITLE$span$4" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$4" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$4');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_5" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$5"><span id="PTSTITLE$span$5" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$5" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$5');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_6" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$6"><span id="PTSTITLE$span$6" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$6" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$6');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_7" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$7"><span id="PTSTITLE$span$7" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$7" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$7');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_8" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$8"><span id="PTSTITLE$span$8" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$8" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$8');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_9" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$9"><span id="PTSTITLE$span$9" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$9" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$9');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_10" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$10"><span id="PTSTITLE$span$10" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$10" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$10');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_11" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$11"><span id="PTSTITLE$span$11" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$11" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$11');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_12" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$12"><span id="PTSTITLE$span$12" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$12" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$12');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_13" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$13"><span id="PTSTITLE$span$13" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$13" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$13');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_14" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$14"><span id="PTSTITLE$span$14" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$14" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$14');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_15" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$15"><span id="PTSTITLE$span$15" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$15" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$15');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_16" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$16"><span id="PTSTITLE$span$16" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$16" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$16');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_17" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$17"><span id="PTSTITLE$span$17" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$17" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$17');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_18" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$18"><span id="PTSTITLE$span$18" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$18" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$18');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_19" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$19"><span id="PTSTITLE$span$19" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$19" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$19');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_20" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$20"><span id="PTSTITLE$span$20" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$20" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$20');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_21" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$21"><span id="PTSTITLE$span$21" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$21" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$21');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_22" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$22"><span id="PTSTITLE$span$22" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$22" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$22');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_23" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$23"><span id="PTSTITLE$span$23" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$23" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$23');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_24" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$24"><span id="PTSTITLE$span$24" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$24" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$24');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_25" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$25"><span id="PTSTITLE$span$25" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$25" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$25');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_26" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$26"><span id="PTSTITLE$span$26" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$26" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$26');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_27" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$27"><span id="PTSTITLE$span$27" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$27" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$27');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_28" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$28"><span id="PTSTITLE$span$28" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$28" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$28');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_29" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$29"><span id="PTSTITLE$span$29" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$29" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$29');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_30" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$30"><span id="PTSTITLE$span$30" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$30" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$30');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_31" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$31"><span id="PTSTITLE$span$31" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$31" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$31');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_32" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$32"><span id="PTSTITLE$span$32" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$32" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$32');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_33" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$33"><span id="PTSTITLE$span$33" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$33" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$33');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_34" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$34"><span id="PTSTITLE$span$34" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$34" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$34');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_35" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$35"><span id="PTSTITLE$span$35" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$35" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$35');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_36" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$36"><span id="PTSTITLE$span$36" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$36" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$36');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_37" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$37"><span id="PTSTITLE$span$37" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$37" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$37');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_38" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$38"><span id="PTSTITLE$span$38" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$38" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$38');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_39" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$39"><span id="PTSTITLE$span$39" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$39" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$39');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_40" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$40"><span id="PTSTITLE$span$40" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$40" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$40');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_41" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$41"><span id="PTSTITLE$span$41" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$41" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$41');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_42" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$42"><span id="PTSTITLE$span$42" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$42" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$42');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_43" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$43"><span id="PTSTITLE$span$43" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$43" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$43');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_44" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$44"><span id="PTSTITLE$span$44" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$44" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$44');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_45" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$45"><span id="PTSTITLE$span$45" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$45" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$45');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_46" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$46"><span id="PTSTITLE$span$46" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$46" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$46');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_47" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$47"><span id="PTSTITLE$span$47" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$47" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$47');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_48" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$48"><span id="PTSTITLE$span$48" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$48" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$48');">Title</a></span></div></li><li class="ps_grid-row ps_box-menuitem" id="PTS_INTELLISRCH_RS$0_row_49" role="presentation">
<div role="presentation" class="ps_box-link pts_result_link" id="win0hdrdivPTSTITLE$49"><span id="PTSTITLE$span$49" class="ps-link-wrapper" role="presentation"><a id="PTSTITLE$49" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PTSTITLE$49');">Title</a></span></div></li></ul></div>
</div></div></div></div></div></div></div></div></div></div><div class=" ps_actions_cont" id="win0hdrdivPT_ACTION_CONT"><div class=" ps_custom_cont  ps_target-custright" id="win0hdrdivPT_CUSTOM_RIGHT"></div><div class=" ps_system_cont" id="win0hdrdivPTLAYOUT_HEADER_GROUPBOX6"><div class="ps_box-group psc_layout ps_header_button ps_search-custom psc_hide-BP3" id="win0hdrdivPT_CUSTOM_SEARCH"></div><div class="ps_box-button psc_image_only psc_toolaction-home ps_header_button ps_header-home psc_hide-BP2" id="win0hdrdivPT_HOME"><span class="ps-button-wrapper" title="Home"><a id="PT_HOME" class="ps-button" role="button" href="javascript:DoHome('https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/s/WEBLIB_PTBR.ISCRIPT1.FieldFormula.IScript_StartPage')" onclick="javascript:cancelBubble(event);"><img src="/cs/hcm/cache/pdhcm_250316/PT_HEADER_HOME_1.svg" id="PT_HOME$IMG" class="ps-img" alt="Home"></a></span></div><div class=" ps_header_button psc_header-all" id="win0hdrdiv$ICField54"><div class="ps_box-group psc_has_popup ps_box-button  psc_menu-act  ps_header_button psc_header-all psc_image_only" id="win0hdrdivPT_ACTION_MENU"><span class="ps-button-wrapper" title="Actions"><a class="ps-button" role="button" id="PT_ACTION_MENU$PIMG" onclick="javascript:cancelBubble(event);" aria-haspopup="true" href="javascript:submitAction_win0(document.win0,'PT_ACTION_MENU');"><span class="ps-text">Actions</span><img class="ps-img" src="/cs/hcm/cache/pdhcm_250316/PT_HEADER_ACTIONS_1.svg" alt=""></a></span><div class="psc_hidden" options="sPopupParentId@PT_ACTION_MENU$PIMG;bPIA@1;bPopup@1;bMask@0;bClose@1;bHeader@1;bCache@1;sStyle@ps_popup-menu ps_menutype-act;sTitle@Actions List Popup;bAutoClose@1;bMask@1;sMaskStyle@ps_masktrans;bVertical@1;bHeader@0;bPopupMenu@1;" id="PT_ACTION_MENU$divpop"><div class="ps_content-group ps_scrollable ps_scrollable_v sbar sbar_v" id="win0hdrdivPT_ACTION_MENUgrp" onscroll="doScroll(this, false);">
<ul role="menu" class="ps_box-group ps_box-menucontainer pt_keynav-list ps_menucontainer" id="win0hdrdiv$ICField13"><li role="presentation" class=" ps_custom_action ps_menusection " id="win0hdrdivPT_CUSTOM_ACTION"></li><li role="presentation" class="  ps_search_action ps_menusection " id="win0hdrdivPT_SEARCH_ACTION"></li><li role="presentation" class=" ps_ag_action ps_menusection " id="win0hdrdivPT_ACTGUIDE_ACTION"></li><li role="presentation" class="ps_box-group psc_layout ps_system_action ps_menusection" id="win0hdrdivPT_SYSTEM_ACTION"><ul role="presentation" class="ps_box-group psc_layout" id="win0hdrdivPT_SYSACT_CONT"><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-previous ps_menuitem psc_hidden" id="win0hdrdivPT_SYSACT_PRVLST"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-next ps_menuitem  psc_hidden" id="win0hdrdivPT_SYSACT_NXTLST"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-retlist ps_menuitem  psc_hidden" id="win0hdrdivPT_SYSACT_RETLST" aria-hidden="true" ps_state="psc_hidden"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_menuitem ptpn_share" id="win0hdrdivPT_SYSACT_SHARE"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-home ps_menuitem psc_show-BP2" id="win0hdrdivPT_SYSACT_HOME"><div role="presentation" class="ps_box-link psc_toolaction-home" id="win0hdrdivPT_HOME_MENU"><span id="PT_HOME_MENU$span" class="ps-link-wrapper" role="presentation"><a id="PT_HOME_MENU" class="ps-link" ptlinktgt="pt_replace" tabindex="-1" role="menuitem" href="javascript:DoHome('https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/s/WEBLIB_PTBR.ISCRIPT1.FieldFormula.IScript_StartPage')" onclick="javascript:cancelBubble(event);">Home</a></span></div></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-gsearch ps_menuitem psc_show-BP3" id="win0hdrdivPT_SYSACT_GBLSRCH"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-addhp ps_menuitem" id="win0hdrdivPT_SYSACT_ADDHP"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-addnb ps_menuitem" id="win0hdrdivPT_SYSACT_ADDNB"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-addfav ps_menuitem" id="win0hdrdivPT_SYSACT_ADDFAV"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-navbar ps_menuitem psc_show-BP4" id="win0hdrdivPT_SYSACT_NAVBAR"><div role="presentation" class="ps_box-link psc_toolaction-navbar" id="win0hdrdivPT_NAVBAR_MENU"><span id="PT_NAVBAR_MENU$span" class="ps-link-wrapper" role="presentation"><a id="PT_NAVBAR_MENU" class="ps-link" onclick="javascript:cancelBubble(event);" href="javascript:DoNavBar(&quot;https://recruiting.calgary.ca/psc/hcm_newwin/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PTNUI_NAVBAR.GBL?ICDoModelessIframe=1&quot;);" ptlinktgt="pt_replace" tabindex="-1" role="menuitem">NavBar</a></span></div></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-mcfconsole ps_menuitem" id="win0hdrdivPT_SYSACT_MCF"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-mypref ps_menuitem" id="win0hdrdivPT_SYSACT_MYPREF"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-access ps_menuitem" id="win0hdrdivPT_SYSACT_ACCESS"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_menuitem" id="win0hdrdivPT_SYSACT_PPM"></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-help ps_menuitem psc_hidden" id="win0hdrdivPT_SYSACT_HELP" aria-hidden="true" ps_state="psc_hidden"><div role="presentation" class="ps_box-link psc_toolaction-help" id="win0hdrdivPT_HELP_MENU"><span id="PT_HELP_MENU$span" class="ps-link-wrapper" role="presentation"><a id="PT_HELP_MENU" class="ps-link" ptlinktgt="pt_replace" tabindex="-1" role="menuitem" href="javascript:DoHelp('PeopleSoft Online Help')" onclick="javascript:cancelBubble(event);">Help</a></span></div></li><li role="presentation" class="ps_box-group ps_box-menuitem ps_header-logout ps_menuitem" id="win0hdrdivPT_SYSACT_LOGOUT"><div role="presentation" class="ps_box-link psc_toolaction-logout" id="win0hdrdivPT_LOGOUT_MENU"><span id="PT_LOGOUT_MENU$span" class="ps-link-wrapper" role="presentation"><a id="PT_LOGOUT_MENU" class="ps-link" ptlinktgt="pt_replace" tabindex="-1" role="menuitem" href="javascript:DoLogout('https://recruiting.calgary.ca/psp/hcm/EMPLOYEE/HRMS/?cmd=logout')" onclick="javascript:cancelBubble(event);">Sign Out</a></span></div></li></ul></li></ul></div></div></div></div><div class="ps_box-button psc_image_only psc_toolaction-navbar ps_header_button hdrnbbtn ps_header-navbar psc_hide-BP4" id="win0hdrdivPT_NAVBAR"><span class="ps-button-wrapper" title="NavBar"><a id="PT_NAVBAR" class="ps-button" onclick="javascript:cancelBubble(event);" href="javascript:DoNavBar(&quot;https://recruiting.calgary.ca/psc/hcm_newwin/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PTNUI_NAVBAR.GBL?ICDoModelessIframe=1&quot;);" role="button"><img src="/cs/hcm/cache/pdhcm_250316/PT_HEADER_NAVBAR_1.svg" id="PT_NAVBAR$IMG" class="ps-img" alt="NavBar"></a></span></div></div></div></div><div class=" ps_pagetitle_cont" id="win0hdrdivPT_TITLE_CONT1"><div class=" ps_system_cont  ps_target-title" id="win0hdrdivPT_PAGETITLE1"><h1 id="PT_PAGETITLE1" class="ps_pagetitle"><span class="ps-text" id="PT_PAGETITLE1lbl">Job Description</span></h1></div><div class=" ps_custom_cont ps_target-custmiddle" id="win0hdrdivPT_CUSTOM_MIDDLE1"></div><div class=" ps_context_cont" id="win0hdrdiv$ICField83"><div class="ps_box-group psc_has_popup ps_box-button psc_menu-act psc_image_only psc_button-transparent psc_image-nomaxheight" id="win0hdrdivPT_CONTEXT_MENU"><span class="ps-button-wrapper" title="More Actions"><a class="ps-button" role="button" id="PT_CONTEXT_MENU$PIMG" onclick="javascript:cancelBubble(event);" aria-haspopup="true" href="javascript:submitAction_win0(document.win0,'PT_CONTEXT_MENU');"><span class="ps-text">More Actions</span><img class="ps-img" src="/cs/hcm/cache/pdhcm_250316/PT_CONTEXT_MENU_ICN_1.SVG" alt=""></a></span><div class="psc_hidden" options="sPopupParentId@PT_CONTEXT_MENU$PIMG;bPIA@1;bPopup@1;bMask@0;bClose@1;bHeader@1;bCache@1;sStyle@ps_popup-menu ps_menutype-act;bAutoClose@1;bMask@1;bVertical@1;bHeader@0;bPopupMenu@1;" id="PT_CONTEXT_MENU$divpop"><div class="ps_content-group ps_scrollable ps_scrollable_v sbar sbar_v" id="win0hdrdivPT_CONTEXT_MENUgrp" onscroll="doScroll(this, false);">
<ul role="menu" class="ps_box-group ps_box-menucontainer pt_keynav-list ps_menucontainer" id="win0hdrdiv$ICField$14$"><li role="presentation" class=" ps_custom_action ps_menusection " id="win0hdrdivPT_CUSTOM_ACTION1"><ul role="presentation" class="ps_box-group ps_menusection hrs_action_menuitem" id="win0divPTLAYOUT_PT_MENU_PRESENT"><li class="ps_box-group psc_layout ps_menuitem " id="win0divPTLAYOUT_PT_MENU_LISTITEM"><div role="presentation" class="ps_box-link" id="win0divDERIVED_HRS_CG_HRS_HOME_PB"><span id="DERIVED_HRS_CG_HRS_HOME_PB$span" class="ps-link-wrapper" role="presentation"><a id="DERIVED_HRS_CG_HRS_HOME_PB" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_HRS_CG_HRS_HOME_PB');">Careers</a></span></div></li><li class="ps_box-group psc_layout  ps_menuitem  " id="win0divPTLAYOUT_PT_MENU_LISTITEM$30$"><div role="presentation" class="ps_box-link" id="win0divDERIVED_HRS_CG_HRS_LOGIN_PB"><span id="DERIVED_HRS_CG_HRS_LOGIN_PB$span" class="ps-link-wrapper" role="presentation"><a id="DERIVED_HRS_CG_HRS_LOGIN_PB" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_HRS_CG_HRS_LOGIN_PB');">Sign In</a></span></div></li><li class="ps_box-group psc_layout  ps_menuitem  " id="win0divPTLAYOUT_PT_MENU_LISTITEM$32$"><div role="presentation" class="ps_box-link" id="win0divDERIVED_HRS_CG_HRS_REGISTER_PB"><span id="DERIVED_HRS_CG_HRS_REGISTER_PB$span" class="ps-link-wrapper" role="presentation"><a id="DERIVED_HRS_CG_HRS_REGISTER_PB" class="ps-link" ptlinktgt="pt_peoplecode" tabindex="-1" role="menuitem" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_HRS_CG_HRS_REGISTER_PB');">New User</a></span></div></li></ul></li><li role="presentation" class="  ps_search_action ps_menusection " id="win0hdrdivPT_SEARCH_ACTION1"></li><li role="presentation" class=" ps_ag_action ps_menusection " id="win0hdrdivPT_ACGUIDE_ACTION1"></li></ul></div></div></div></div></div></div><div class="ps_box-group psc_layout ps_header_confirmation" id="win0hdrdivPT_CONFIRM_CONT"><div role="alert" aria-live="assertive" class="ps_box-group psc_layout psc_confirmation-animate " id="win0hdrdivPT_CONFIRMATION"><div class="ps_box-group psc_layout psc_confirmation-area" id="win0hdrdivPT_CONFIRM_AREA"><div class="ps_box-longedit psc_disabled psc_wrappable psc_has_value psc_confirmation-msg" id="win0hdrdivPT_CONFIRM_MSG"><div class="ps_box-label" id="win0hdrdivPT_CONFIRM_MSGlbl"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="PT_CONFIRM_MSG">&nbsp;</span>
</div><div class="ps_box-button psc_image_only psc_modal-close psc_confirmation-close" id="win0hdrdivPT_CONFIRM_CLOSE"><span class="ps-button-wrapper" title="Close"><a id="PT_CONFIRM_CLOSE" class="ps-button" role="button" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'PT_CONFIRM_CLOSE');"><img src="/cs/hcm/cache/pdhcm_250316/PT_MODAL_CLOSE_NUI_1.svg" id="PT_CONFIRM_CLOSE$IMG" class="ps-img" alt="Close"></a></span></div></div></div></div><div class="ps_box-group psc_layout ps_ag-processheader" id="win0hdrdivPT_AG_LAYOUT_PT_AG_GROUPBOX3"></div><div class=" ps_header_bar_custom ps_target-custbottom" id="win0hdrdivPT_CUSTOM_BOTTOM"></div></div></div></div>

</div>
<div class="ps_search psc_close side" id="PT_SEARCH"></div>
<div class="ps_box-pagetabs psc_hidden" id="win0divPSPANELTABS"></div>

<div class="ps_mid_section" id="PT_MID_SECTION">
<div class="pst_panel-side1" id="PT_SIDE"><div class="pst_panel-side1-top" id="PT_SIDE_TOP"></div><div class="pst_panel-side1-bottom" id="PT_SIDE_BOTTOM"></div></div>

<div class="ps_content" id="PT_CONTENT" role="main">
<div class="ps_main" id="PT_MAIN"><div class="ps_pagecontainer" id="win0divPAGECONTAINER">
<div class="ps_pspagecontainer" id="win0divPSPAGECONTAINER">
<div class="ps_box-group psc_layout psc_page-container" id="win0divDERIVED_HRS_CG_HRS_GRPBOX_00"><div class="ps_box-group psc_layout psc_flex-none" id="win0divDERIVED_HRS_CG_HRS_GRPBOX_01"><div class="ps_box-group psc_layout" id="win0div$ICField1"><div class="ps_box-group psc_layout ps_apps_pageheader psc_pageheader-fixed" id="win0divHRS_SCH_WRK_FLU_HRS_GRPBOX_07"><div class="ps_box-group psc_layout" id="win0divDERIVED_HRS_FLU_"><div class="ps_box-group psc_layout psc_float-right hrs_cg_margin-topn3em" id="win0divDERIVED_HRS_CG_"></div></div><div class="ps_box-group psc_layout" id="win0divHRS_SCH_WRK_FLU_HRS_GRPBOX_06"><div class="ps_box-group psc_layout hrs_flexRow psc_margin-top02em" id="win0div$ICField30"><div class="ps_box-link psc_disabled" id="win0divDERIVED_HRS_FLU_HRS_PREVIOUS_PB"><span class="ps-link-wrapper" title="Previous"><a id="DERIVED_HRS_FLU_HRS_PREVIOUS_PB" aria-disabled="true" disabled="disabled" class="ps-link"><img src="/cs/hcm/cache/pdhcm_250316/PT_GUIDED_PREV_ICON_ALT_1.svg" id="DERIVED_HRS_FLU_HRS_PREVIOUS_PB$IMG" class="ps-img" alt=""><span class="ps-text">Previous Job</span></a></span></div><div class="ps_box-group psc_layout psc_nolabel hrs_flex psc_strong psc_halign-center psc_margin-none" id="win0divDERIVED_HRS_FLU_GROUPBOX12"><div class="ps_box-group psc_layout psc_nolabel hrs_flex psc_strong psc_halign-center psc_margin-none" id="win0divDERIVED_HRS_FLU_GROUPBOX11"><div class="ps_box-edit psc_disabled psc_wrappable psc_has_value psc_nolabel hrs_flex psc_strong psc_halign-center psc_margin-none" id="win0divHRS_SCH_WRK2_POSTING_TITLE"><div class="ps_box-label" id="win0divHRS_SCH_WRK2_POSTING_TITLElbl"><span class="ps-label">Job Title</span></div><span class="ps_box-value" id="HRS_SCH_WRK2_POSTING_TITLE">Senior Accountant</span>
</div></div></div><div class="ps_box-link psc_disabled  psc_float-right" id="win0divDERIVED_HRS_FLU_HRS_NEXT_PB"><span class="ps-link-wrapper" title="Next"><a id="DERIVED_HRS_FLU_HRS_NEXT_PB" aria-disabled="true" disabled="disabled" class="ps-link"><span class="ps-text">Next Job</span><img src="/cs/hcm/cache/pdhcm_250316/PT_GUIDED_NEXT_ICON_ALT_1.svg" id="DERIVED_HRS_FLU_HRS_NEXT_PB$IMG" class="ps-img" alt=""></a></span></div></div></div></div></div></div><div class="ps_box-group psc_layout ps_apps_content" id="win0divDERIVED_HRS_CG_HRS_GRPBOX_02"><div class="ps_box-group psc_layout hrs_cg_page_width_1440 " id="win0div$ICField189"><div class="ps_box-group psc_layout hrs_top-button-box" id="win0div$ICField181"><div class="ps_box-button psc_primary psc_float-right" id="win0divAPPLYJOB"><span id="APPLYJOB$span" class="ps-button-wrapper" title="Apply"><a id="APPLYJOB" class="ps-button" role="button" ptlinktgt="pt_peoplecode" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'APPLYJOB');">Apply for Job</a></span></div></div><div class="ps_box-group" id="win0div$ICField166"><div class="ps_box-group psc_layout  psc_column-2 " id="win0div$ICField169"><div class="ps_box-group psc_layout psc_columnitem-1of2 " id="win0div$ICField167"><div class="ps_box-edit psc_disabled psc_has_value psc_num" id="win0divHRS_SCH_WRK2_HRS_JOB_OPENING_ID"><div class="ps_box-label" id="win0divHRS_SCH_WRK2_HRS_JOB_OPENING_IDlbl"><span class="ps-label">Job ID</span></div><span class="ps_box-value" id="HRS_SCH_WRK2_HRS_JOB_OPENING_ID">312471</span>
</div><div class="ps_box-longedit psc_disabled psc_wrappable psc_has_value" id="win0divHRS_SCH_WRK_HRS_DESCRLONG"><div class="ps_box-label" id="win0divHRS_SCH_WRK_HRS_DESCRLONGlbl"><span class="ps-label">Location</span></div><span class="ps_box-value" id="HRS_SCH_WRK_HRS_DESCRLONG">Calgary, Alberta, Canada</span>
</div></div><div class="ps_box-group psc_layout psc_columnitem-1of2 " id="win0div$ICField168"><div class="ps_box-edit psc_disabled psc_has_value" id="win0divHRS_SCH_WRK_HRS_FULL_PART_TIME"><div class="ps_box-label" id="win0divHRS_SCH_WRK_HRS_FULL_PART_TIMElbl"><span class="ps-label">Full/Part Time</span></div><span class="ps_box-value" id="HRS_SCH_WRK_HRS_FULL_PART_TIME">Full-Time</span>
</div><div class="ps_box-edit psc_disabled psc_has_value" id="win0divHRS_SCH_WRK_HRS_REG_TEMP"><div class="ps_box-label" id="win0divHRS_SCH_WRK_HRS_REG_TEMPlbl"><span class="ps-label">Regular/Temporary</span></div><span class="ps_box-value" id="HRS_SCH_WRK_HRS_REG_TEMP">Temporary</span>
</div></div></div></div><div class="ps_box-group psc_layout psc_padding-left12pct  psc_bordert" id="win0div$ICField132"><div class="ps_box-group psc_layout psc_margin-top05em" id="win0div$ICField165"><div class="ps_box-group psc_layout psc_margin-bottom1em psc_margin-top1em" id="win0divHRS_SCH_WRK2_HRS_FAVORITE_ICN"><div class="ps_box-link  psc_label-valignmiddle " id="win0divHRS_SCH_WRK2_HRS_FAVORITE_ICN$128$"><span class="ps-link-wrapper" title="Add to My Favorite Jobs"><a id="HRS_SCH_WRK2_HRS_FAVORITE_ICN$128$" class="ps-link" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'HRS_SCH_WRK2_HRS_FAVORITE_ICN$128$');"><img src="/cs/hcm/cache/pdhcm_250316/PS_FAVORITE_DISABLED_ICN_1.png" id="HRS_SCH_WRK2_HRS_FAVORITE_ICN$128$$IMG" class="ps-img" alt=""><span class="ps-text">Add to My Favorite Jobs</span></a></span></div></div><div class="ps_box-group psc_layout psc_margin-bottom1em" id="win0divHRS_SCH_WRK_HRS_CE_EML_FRND"><div class="ps_box-link psc_label-valignmiddle" id="win0divHRS_SCH_WRK_HRS_CE_EML_FRND$148$"><span class="ps-link-wrapper" title="Email to Friend"><a id="HRS_SCH_WRK_HRS_CE_EML_FRND$148$" class="ps-link" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'HRS_SCH_WRK_HRS_CE_EML_FRND$148$');"><img src="/cs/hcm/cache/pdhcm_250316/PS_EMAIL_S_FL_1.svg" id="HRS_SCH_WRK_HRS_CE_EML_FRND$148$$IMG" class="ps-img" alt=""><span class="ps-text">Email this Job</span></a></span></div></div></div><div class="ps_box-group psc_layout hrs_sr-only" id="win0divDERIVED_HRS_CG_HRS_GRPBOX_04"><div class="ps_box-edit psc_disabled psc_has_value" id="win0divHRS_SCH_WRK2_DESCR254"><div class="ps_box-label" id="win0divHRS_SCH_WRK2_DESCR254lbl"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="HRS_SCH_WRK2_DESCR254">&nbsp;</span>
</div></div></div><div class="ps_box-group psc_layout psc_bordert" id="win0div$ICField188"><div class="ps_box-scrollarea" id="win0divHRS_SCH_PSTDSC$0"><div class="ps_box-scrollarea-row" id="win0divHRS_SCH_PSTDSC_row$0"><div class="ps_box-group hrs_cg_groupbox_field_label_back" id="win0divHRS_SCH_WRK_DESCR100$0"><div class="ps_box-longedit psc_disabled psc_has_valueasrte psc_nolabel psc_wrappable" id="win0divHRS_SCH_PSTDSC_DESCRLONG$0"><div class="ps_box-label" id="win0divHRS_SCH_PSTDSC_DESCRLONGlbl$0"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="HRS_SCH_PSTDSC_DESCRLONG$0">
<div><div style="line-height:normal;margin-bottom:0pt;margin-right:0in;margin-top:0in;"><span style="background-color:white;color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">If you are committed to public service, enjoy collaborating with others, share our values and have a desire to learn and grow, join</span></span><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;"> </span></span><a target="_blank" rel="noopener noreferrer" href="http://www.calgary.ca/CA/city-manager/Pages/About-Us/ourcity.aspx#whyWeAreHere"><span style="background-color:white;color:rgb(51,102,204);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">The City of Calgary</span></span></a><span style="background-color:white;color:black;"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">. </span></span><span style="background-color:white;color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">City employees deliver the services, run the programs and operate the facilities which make a difference in our community. We support work-life balance, promote physical and psychological safety, and offer competitive wages, pensions, and </span></span><a target="_blank" rel="noopener noreferrer" href="http://www.calgary.ca/cfod/hr/Pages/Careers/Benefits.aspx"><span style="background-color:white;color:rgb(0,102,204);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">benefits</span></span></a><span style="background-color:white;color:black;"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">. </span></span><span style="background-color:white;color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Together we make Calgary a great place to make a living, a great place to make a life.</span></span></div><div style="line-height:normal;margin-bottom:0pt;margin-right:0in;margin-top:0in;">&nbsp;</div><div style="line-height:normal;margin:0in 0in 0pt;"><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">The City is committed to fostering a respectful, inclusive and equitable workplace which is representative of the community we serve. We welcome those who have demonstrated a commitment to upholding the values of equity, diversity, inclusion, anti-racism and reconciliation. Applications are encouraged from members of groups that are historically disadvantaged and underrepresented. Accommodations are available during the hiring process, upon request.&nbsp;</span></span></div></div></span>
</div></div></div><div class="ps_box-scrollarea-row" id="win0divHRS_SCH_PSTDSC_row$1"><div class="ps_box-group hrs_cg_groupbox_field_label_back" id="win0divHRS_SCH_WRK_DESCR100$1"><div class="ps_box-longedit psc_disabled psc_has_valueasrte psc_nolabel psc_wrappable" id="win0divHRS_SCH_PSTDSC_DESCRLONG$1"><div class="ps_box-label" id="win0divHRS_SCH_PSTDSC_DESCRLONGlbl$1"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="HRS_SCH_PSTDSC_DESCRLONG$1">
<p class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">As the Senior Accountant (SA), you will provide support to the Financial Accounting Services Team to ensure complete and accurate processing of financial data, address financial reporting and audit requests and maintain the appropriate financial records. In </span><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;" lang="EN-CA">this position, you will support finance teams across business units by handling a range of financing, budgeting, and master data tasks. The SA is also responsible for managing financial data within core accounting and budgeting systems, as well as fulfilling financial reporting and auditing requests. Primary duties include:</span></p><ul><li class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Process routine and ad-hoc journal entries, maintain month-end and year-end processes and financial schedules, prepare monthly, interim and year-end financial statements and supporting documentation.</span><o:p></o:p></li><li class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Support year-end and interim external and internal audit requests, participate in control testing walkthroughs.&nbsp;</span><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;mso-spacerun:yes;" lang="EN-CA">&nbsp;</span><o:p></o:p></li><li class="MsoNoSpacing"><span style="font-family:Symbol;font-size:10.5pt;font:7.0pt &quot;Times New Roman&quot;;mso-bidi-font-family:Symbol;mso-bidi-font-weight:bold;mso-fareast-font-family:Symbol;mso-list:Ignore;" lang="EN-CA">&nbsp;</span><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Prepare and maintain detailed capital financing schedules for assigned business units, ensure alignment with Portfolio Finance funding guidelines and accurate tracking of capital allocations and projects.</span><o:p></o:p></li><li class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Build and maintain effective working relationships with Portfolio and other customers by responding promptly and professionally to both routine and ad-hoc financial inquiries. Present financial data in a clear and professional manner, translating complex information into accessible formats.</span><o:p></o:p></li><li class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Provide training, mentoring and guidance to Junior Accountants. Participate in peer-to-peer review activities to assess and validate work completed by other Senior Accountants.</span></li><li class="MsoNoSpacing"><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Collaborate with colleagues and Portfolio partners to plan for workload coverage during staff absences or peak operational demands.</span></li></ul></span>
</div></div></div><div class="ps_box-scrollarea-row" id="win0divHRS_SCH_PSTDSC_row$2"><div class="ps_box-group hrs_cg_groupbox_field_label_back" id="win0divHRS_SCH_WRK_DESCR100$2"><div class="ps_box-longedit psc_disabled psc_has_valueasrte psc_nolabel psc_wrappable" id="win0divHRS_SCH_PSTDSC_DESCRLONG$2"><div class="ps_box-label" id="win0divHRS_SCH_PSTDSC_DESCRLONGlbl$2"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="HRS_SCH_PSTDSC_DESCRLONG$2">
<div><span style="color:rgb(51,51,102);"><span class="PT_RTE_DISPLAYONLY PABOLDREDTEXT" style="font-family:Arial,Helvetica,sans-serif;font-size:14px;" id="HRS_JO_WRK_POSTING_TITLE$0"><strong>Qualifications&nbsp;</strong></span></span></div><ul><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">A degree in Business Administration or Commerce with a major in accounting and at least 14 completed post secondary accounting and business courses recognized by Chartered Professional Accountants (CPA) program OR;</span><o:p></o:p></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Enrolled in CPA Professional Education Program (PEP) and working towards the CPA designation.&nbsp;</span></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">At least 5 years of relevant experience in full cycle accounting or bookkeeping experience in a mid to large size finance team; preparing interim and year-end financial schedules, reconciliations and financial statements; interpreting and applying financial policies, procedures and accounting standards; and interacting with auditors to facilitate internal and external audits, controls testing and other reviews.</span><o:p></o:p></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Technical accounting skills including preparing and analyzing complex data, schedules, and year-end financial statements and working papers.</span><o:p></o:p></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Intermediate proficiency in Microsoft Office (Excel and Word) is required.</span><o:p></o:p></li><li><span style="font-family:Symbol;font-size:10.5pt;font:7.0pt &quot;Times New Roman&quot;;mso-bidi-font-family:Symbol;mso-bidi-font-weight:bold;mso-fareast-font-family:Symbol;mso-list:Ignore;" lang="EN-CA">&nbsp;</span><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Working knowledge of PeopleSoft Financial and Supply Chain Management (FSCM), Human Capital Management (HCM) and Hyperion (Budget Planning and Reporting); Oracle SmartView for Microsoft Office will be considered assets.</span><o:p></o:p></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Demonstrates analytical and problem-solving skills.</span><o:p></o:p></li><li><span style="font-family:&quot;Arial&quot;,sans-serif;font-size:10.5pt;mso-bidi-font-weight:bold;" lang="EN-CA">Excellent communication and interpersonal skills, and the ability to work effectively in a team environment.</span><o:p></o:p></li></ul><div>&nbsp;</div><div><span style="color:rgb(51,51,102);"><span class="PT_RTE_DISPLAYONLY PABOLDREDTEXT" style="font-family:Arial,Helvetica,sans-serif;font-size:14px;"><strong>Pre-employment Requirements&nbsp;</strong></span></span></div><div><ul><li style="line-height:normal;margin:0in 0in 0pt;"><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Successful applicants must provide proof of qualifications.</span></span></li></ul><p style="font-family:Arial;font-size:10.5pt;margin:0in;"><span style="color:#333366;"><strong>Workstyle: </strong></span><span style="color:black;">This position may be eligible to work from home for at least part of the time as one of several flexible work options available to City employees. These arrangements depend on the operational requirements of the role, employee suitability, and are subject to change based on operational needs and corporate direction.&nbsp;</span></p></div></span>
</div></div></div><div class="ps_box-scrollarea-row" id="win0divHRS_SCH_PSTDSC_row$3"><div class="ps_box-group hrs_cg_groupbox_field_label_back" id="win0divHRS_SCH_WRK_DESCR100$3"><div class="ps_box-longedit psc_disabled psc_has_valueasrte psc_nolabel psc_wrappable" id="win0divHRS_SCH_PSTDSC_DESCRLONG$3"><div class="ps_box-label" id="win0divHRS_SCH_PSTDSC_DESCRLONGlbl$3"><span class="ps-label">&nbsp;</span></div><span class="ps_box-value" id="HRS_SCH_PSTDSC_DESCRLONG$3">
<div>&nbsp;</div><div>&nbsp;</div><figure class="table"><table style="width:750px;" align="center" border="1" cellpadding="1" cellspacing="1"><tbody><tr><td><figure class="table"><table style="width:750px;" border="0" cellpadding="1" cellspacing="1"><tbody><tr><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Union: CUPE Local 38</span></span></div></td><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Business Unit: Finance</span></span></div></td></tr><tr><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Position Type: 4 Temporary (up to 12 months)&nbsp;</span></span></div></td><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Location:</span></span><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;"> 800 Macleod Trail SE</span></div></td></tr><tr><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Compensation: Pay Grade&nbsp;10 $42.62 - 56.97 per hour&nbsp;</span></span></div></td><td style="vertical-align:top;" rowspan="2"><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Days of Work: This position typically works a 5 day</span></span><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">&nbsp;</span></div><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">work week, with 1 day off in each 3 week cycle.</span></span><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">&nbsp;</span></div></td></tr><tr><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Hours of work: Standard 35 hour work week</span></span><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">&nbsp;</span></div></td></tr><tr><td><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Audience: Internal/External&nbsp;</span></span></div></td><td style="vertical-align:top;"><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Apply By: August 28, 2025</span></span></div></td></tr><tr><td><div>&nbsp;</div></td><td style="vertical-align:top;"><div><span style="color:rgb(0,0,0);"><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;">Job ID #:</span></span><span style="font-family:Arial,Helvetica,sans-serif;font-size:14px;"> 312471</span></div></td></tr></tbody></table></figure></td></tr></tbody></table></figure><div style="text-align:center;"><div style="line-height:normal;"><div style="line-height:normal;"><div style="line-height:normal;">&nbsp;</div></div></div></div></span>
</div></div></div></div></div></div></div><div class="ps_box-group psc_hidden" id="win0div$ICField41"><div class="ps_box-button psc_primary psc_margin-05em" id="win0divHRS_SCH_WRK_HRS_APPLY_PB"><span id="HRS_SCH_WRK_HRS_APPLY_PB$span" class="ps-button-wrapper" title="Apply"><a id="HRS_SCH_WRK_HRS_APPLY_PB" class="ps-button" role="button" ptlinktgt="pt_peoplecode" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'HRS_SCH_WRK_HRS_APPLY_PB');">Apply for Job</a></span></div></div><div class="ps_box-group psc_layout psc_hidden" id="win0div$ICField17"></div><div class="ps_box-group psc_layout" id="win0div$ICField$2$"><div class="ps_box-group psc_layout psc_hidden" id="win0div$ICField3"><div class="ps_box-htmlarea" id="win0divHRS_CB_WRK_HTMLAREA"><div class="ps-htmlarea">
<!-- Begin HTML Area Name Undisclosed -->

<!-- End HTML Area -->
</div>
</div></div></div></div></div></div>
</div>

</div>
<div class="pst_panel-side2" id="PT_SIDE2"></div>

</div><div class="ps_footer" id="PT_FOOTER"></div>
<div id="DetachDiv" height="0" width="0" frameborder="0"></div>
</div>
<a class="ps-anchor" id="ICLastAnchor_win0"></a>
</form>

<script language="JavaScript">
var bMDTargetStart=false;
var bMDTarget=false;
if (typeof(setPSTouchHandlerDoc) != 'undefined' && setPSTouchHandlerDoc != null) setPSTouchHandlerDoc ();
var nMaxSavedStates=5;
bSearchDialog_empty =false;
var sHistURL="https://recruiting.calgary.ca/psc/hcm/EMPLOYEE/HRMS/c/HRS_HRAM_FL.HRS_CG_SEARCH_FL.GBL?page=HRS_APP_JBPST_FL&FOCUS=Applicant&Page=HRS_APP_JBPST_FL&JobOpeningId=312471&PostingSeq=1&SiteId=1&";
var bCloseModal = false;
var bICList = false;
var bHtml5Doc = true;
var bClearBackState=false;
var bPageTransfered=true;
var bTransferAnimate=false;
var bCleanHtml = false;
var bDefer = true;
document.deferFldArr_win0 = new Array();
document.hiddenFldArr_win0 =new Array('ICType','ICElementNum','ICStateNum','ICAction','ICModelCancel','ICXPos','ICYPos','ResponsetoDiffFrame','TargetFrameName','FacetPath','ICFocus','ICSaveWarningFilter','ICChanged','ICSkipPending','ICAutoSave','ICResubmit','ICSID','ICActionPrompt','ICBcDomData','ICDNDSrc','ICPanelHelpUrl','ICPanelName','ICPanelControlStyle','ICFind','ICAddCount','ICAppClsData');
document.chgFldArr_win0 = new Array();
AddToHistory('Job Description', '', 'returntolastpage@1', 'HRS_APP_JBPST_FL', 2, 0, 0, 0,'',0, '', 1);
corsHistoryTansaction();
var bCleanHtml = true;
var bDefer = true;
document.hiddenFldArr_win0 =new Array('ICType','ICElementNum','ICStateNum','ICAction','ICModelCancel','ICXPos','ICYPos','ResponsetoDiffFrame','TargetFrameName','FacetPath','ICFocus','ICSaveWarningFilter','ICChanged','ICSkipPending','ICAutoSave','ICResubmit','ICSID','ICActionPrompt','ICBcDomData','ICDNDSrc','ICPanelHelpUrl','ICPanelName','ICPanelControlStyle','ICFind','ICAddCount','ICAppClsData');
document.chgFldArr_win0 = new Array();
var bCDATA = false;
var bAccessibleLayout = false;
var bLoadCompleted = true;
</script><div id="divdobackclassic" style="visibility:hidden" aria-hidden="true"><a id="ancdobackclassic" href="javascript:DoBack('win0')" style="visibility:hidden" aria-hidden="true"></a></div>
</body></html>
            ```
            