package com.poas.ui;

import com.example.poas.R;

import android.os.Bundle;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.ProgressDialog;
import android.graphics.Bitmap;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.CookieManager;
import android.webkit.CookieSyncManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

@SuppressLint("SetJavaScriptEnabled")
public class MainActivity extends Activity {
	final class WebClient extends WebViewClient {

		@Override
		public boolean shouldOverrideUrlLoading(WebView view, String url) {
			view.loadUrl(url);
			return true;
		}

		@Override
		public void onPageFinished(WebView view, String url) {
			super.onPageFinished(view, url);
			_processDialog.hide();
		}

		@Override
		public void onPageStarted(WebView view, String url, Bitmap favicon) {
			super.onPageStarted(view, url, favicon);
			_processDialog.show();
		}

	}

	final String LOCAL_BASE = "file:///android_asset";
	final String HOME_URL = "/dossier/index.html";
	final String LOGIN_URL = "/dossier/index.html";
	final String HELP_URL = "/help.html";

	WebView _webView = null;
	WebClient _webClient = null;
	WebInterface _webInterface = null;
	Settings _settings = null;
	ProgressDialog _processDialog = null;

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		initialize();
	}

	@SuppressLint({ "HandlerLeak" })
	private void initialize() {
		this._settings = Settings.instance(this.getApplication());
		this._webInterface = new WebInterface(this._settings);
		this._webClient = new WebClient();
		this._processDialog = new ProgressDialog(this);
		this._processDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
		this._processDialog.setMessage("载入中...");

		_webView = (WebView) findViewById(R.id.webView_content);

		WebSettings settings = this._webView.getSettings();
		settings.setJavaScriptEnabled(true);
		settings.setSaveFormData(false);
		settings.setSavePassword(false);
		settings.setSupportZoom(false);
		settings.setDomStorageEnabled(true);

		this._webView.setWebViewClient(this._webClient);
		this._webView.addJavascriptInterface(this._webInterface, "interface");

		// 提取cookie
		Bundle bundle = this.getIntent().getExtras();
		String cookie = bundle.get("cookie").toString();
		// 设置cookie
		CookieSyncManager syncManager = CookieSyncManager
				.createInstance(this._webView.getContext());
		CookieManager cookieManager = CookieManager.getInstance();
		cookieManager.setAcceptCookie(true);
		cookieManager.removeSessionCookie();
		cookieManager.setCookie("http://" + _settings.get("address", ""),
				cookie);
		syncManager.sync();
		// 加载主页
		navigate_local(LOGIN_URL);
	}

	private void navigate_local(String url) {
		this._webView.loadUrl(LOCAL_BASE + url);
	}

	private void navigate_remote(String url) {
		String re_addr = _settings.get("address", "10.250.62.6");
		if (!re_addr.startsWith("http://")) {
			re_addr = "http://" + re_addr;
		}
		final String address = re_addr;
		final String abs_url = address + url;
		if (Network.isNetworkAvailable(this)) {
			_webView.loadUrl(abs_url);
		} else {
			Toast.makeText(getApplicationContext(), "请连接网络", Toast.LENGTH_SHORT)
					.show();
		}

	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		CharSequence cs = item.getTitle();
		String title = cs.toString();
		Log.d("onOptionItemSelected", title);
		if (title == "退出") {
			this.finish();
		}
		if (title == "舆情") {
			this.navigate_local(HOME_URL);
		}
		if (title == "设置") {
			this.navigate_local("/setting.html");
		}
		if (title == "发送") {
			this.navigate_remote("/admin/");
		}
		if (title == "帮助") {
			this.navigate_local(HELP_URL);
		}

		return true;
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		menu.add(Menu.NONE, Menu.FIRST, 1, "舆情").setIcon(
				android.R.drawable.ic_menu_delete);
		menu.add(Menu.NONE, Menu.FIRST, 2, "设置").setIcon(
				android.R.drawable.ic_menu_edit);
		menu.add(Menu.NONE, Menu.FIRST, 3, "帮助").setIcon(
				android.R.drawable.ic_menu_help);
		menu.add(Menu.NONE, Menu.FIRST, 4, "添加").setIcon(
				android.R.drawable.ic_menu_add);
		menu.add(Menu.NONE, Menu.FIRST, 5, "发送").setIcon(
				android.R.drawable.ic_menu_send);
		menu.add(Menu.NONE, Menu.FIRST, 6, "退出").setIcon(
				android.R.drawable.ic_menu_close_clear_cancel);
		return true;
	}
}
