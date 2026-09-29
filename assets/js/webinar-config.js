/* Paste your deployed Google Apps Script web app URL below.
   In Apps Script also set SPREADSHEET_ID (see scripts/google-apps-script/webinar-registration.gs). */
window.WEBINAR_CONFIG = {
  googleScriptUrl: 'https://script.google.com/macros/s/AKfycbxLP9fRGMST-Tooc0AoRRvEqI9YjqZUVQ1gJyf4jbTYoE15AThZXi402TSKzfC5iZ_x/exec',
  /** ₹99 payment — user is sent here after the form is saved. */
  razorpayPaymentLink: 'https://rzp.io/rzp/qhwE712t',
  /**
   * After successful payment, Razorpay redirects here (set the same URL in Dashboard:
   * Payment Links → your link → Redirect after payment). Leave empty to use /webinar/welcome on current site.
   */
  thankYouPageUrl: '',
  registrationFeeInr: 99
};
