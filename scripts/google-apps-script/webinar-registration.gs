/**
 * CureSoulLife — Webinar registration → Google Sheets
 *
 * SETUP:
 * 1. Open your Google Sheet and copy the ID from the URL:
 *    https://docs.google.com/spreadsheets/d/PASTE_THIS_PART/edit
 * 2. Paste it in SPREADSHEET_ID below.
 * 3. Run testWriteRow() once in Apps Script → approve permissions.
 * 4. Deploy → Manage deployments → Edit → New version → Deploy.
 */

// REQUIRED: paste your Google Sheet ID here
var SPREADSHEET_ID = '';

var SHEET_NAME = 'Registrations';

function doGet(e) {
  try {
    if (e && e.parameter && e.parameter.full_name) {
      return handleSubmission_(e.parameter);
    }
    return jsonResponse_({ ok: true, message: 'Webinar registration endpoint is live.' });
  } catch (err) {
    return jsonResponse_({ ok: false, error: String(err) });
  }
}

function doPost(e) {
  try {
    var data = {};

    if (e && e.parameter && e.parameter.full_name) {
      data = e.parameter;
    } else if (e && e.postData && e.postData.contents) {
      data = JSON.parse(e.postData.contents);
    } else {
      throw new Error('No form data received.');
    }

    return handleSubmission_(data);
  } catch (err) {
    return jsonResponse_({ ok: false, error: String(err) });
  }
}

function handleSubmission_(data) {
  var sheet = getSheet_();
  ensureHeaders_(sheet);

  sheet.appendRow([
    data.timestamp || new Date().toISOString(),
    data.full_name || '',
    data.mobile || '',
    data.email || '',
    data.city || '',
    data.profession || '',
    data.assessment_score || '',
    data.source || 'Life Reset Masterclass'
  ]);

  var ss = getSpreadsheet_();

  return jsonResponse_({
    ok: true,
    saved: true,
    spreadsheet: ss.getName(),
    tab: sheet.getName(),
    row: sheet.getLastRow()
  });
}

function getSpreadsheet_() {
  if (SPREADSHEET_ID) {
    return SpreadsheetApp.openById(SPREADSHEET_ID);
  }

  var ss = SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) {
    throw new Error('Set SPREADSHEET_ID at the top of the Apps Script file.');
  }
  return ss;
}

function getSheet_() {
  var ss = getSpreadsheet_();
  var sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }

  return sheet;
}

function ensureHeaders_(sheet) {
  if (sheet.getLastRow() === 0) {
    sheet.appendRow([
      'Timestamp',
      'Full Name',
      'Mobile',
      'Email',
      'City',
      'Profession',
      'Assessment Score',
      'Source'
    ]);
    sheet.getRange(1, 1, 1, 8).setFontWeight('bold');
  }
}

function jsonResponse_(payload) {
  return ContentService
    .createTextOutput(JSON.stringify(payload))
    .setMimeType(ContentService.MimeType.JSON);
}

/** Run once to verify setup. Results appear in View → Execution log (not a popup). */
function testWriteRow() {
  if (!SPREADSHEET_ID) {
    throw new Error(
      'SPREADSHEET_ID is empty. Open your Google Sheet, copy the ID from the URL, ' +
      'and paste it at the top of this file. Example: ' +
      'https://docs.google.com/spreadsheets/d/YOUR_ID_HERE/edit'
    );
  }

  var result = handleSubmission_({
    timestamp: new Date().toISOString(),
    full_name: 'Apps Script Test',
    mobile: '0000000000',
    email: 'test@curesoullife.org',
    city: 'Test',
    profession: 'Test',
    assessment_score: '0',
    source: 'Manual Test'
  });

  var payload = JSON.parse(result.getContent());
  var ss = getSpreadsheet_();
  var sheet = getSheet_();

  Logger.log('SUCCESS — test row added');
  Logger.log('Spreadsheet: ' + ss.getName());
  Logger.log('Tab: ' + sheet.getName());
  Logger.log('Row number: ' + payload.row);
  Logger.log('Open this sheet: ' + ss.getUrl());

  try {
    SpreadsheetApp.getUi().alert(
      'Test row added successfully!\n\n' +
      'Spreadsheet: ' + ss.getName() + '\n' +
      'Tab: ' + sheet.getName() + '\n' +
      'Row: ' + payload.row + '\n' +
      'URL: ' + ss.getUrl()
    );
  } catch (uiErr) {
    Logger.log('Popup not available from this editor — check Execution log above.');
  }
}
