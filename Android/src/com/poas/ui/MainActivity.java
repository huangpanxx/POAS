package com.poas.ui;

import com.example.poas.R;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.ProgressDialog;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.widget.Toast;

@SuppressLint("SetJavaScriptEnabled")
public class MainActivity extends Activity {
	final class WebClient extends WebChromeClient {

	}

	final String LOCAL_BASE = "file:///android_asset";
	final String HOME_URL = "/dossier/index.html";
	final String LOGIN_URL = "/dossier/index.html";
	final String HELP_URL = "/help.html";

	WebView _webView = null;
	WebClient _webClient = null;
	WebInterface _webInterface = null;
	Handler _handler = null;
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
		this._processDialog.setMessage("载入中，请稍候！");

		this._handler = new Handler() {
			public void handleMessage(Message msg) {
				if (!Thread.currentThread().isInterrupted()) {
					switch (msg.what) {
					case 0:
						_processDialog.show();
						break;
					case 1:
						_processDialog.hide();
						break;
					}
				}
				super.handleMessage(msg);
			}
		};
		_webView = (WebView) findViewById(R.id.webView_content);

		WebSettings settings = this._webView.getSettings();
		settings.setJavaScriptEnabled(true);
		settings.setSaveFormData(false);
		settings.setSavePassword(false);
		settings.setSupportZoom(false);
		settings.setDomStorageEnabled(true);
		this._webView.setWebChromeClient(this._webClient);
		this._webView.addJavascriptInterface(this._webInterface, "interface");

		navigate_local(LOGIN_URL);
	}

	private void navigate_local(String url) {
		this._webView.loadUrl(LOCAL_BASE + url);
	}

	private void navigate_remote(String url) {
		final String address = _settings.get("address", "10.250.62.6");
		final String abs_url = address + url;
		if (Network.isNetworkAvailable(this)) {
			new Thread() {
				public void run() {
					_handler.sendEmptyMessage(0);
					_webView.loadUrl(abs_url);
					_handler.sendEmptyMessage(1);
				}
			}.start();
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
