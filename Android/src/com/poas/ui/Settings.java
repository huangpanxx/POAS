package com.poas.ui;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;

import android.app.Application;
import android.util.Base64;
import android.util.Log;

public class Settings {
	Application _app = null;
	String _fileName = null;
	HashMap<String, String> _map = null;

	private static Settings _instance = null;
	private final static String SETTING_FILE = "settings.ini";

	public static Settings instance(Application app) {
		if (null == _instance) {
			_instance = new Settings(app, SETTING_FILE);
		}
		return _instance;

	}

	private Settings(Application app, String fileName) {
		this._app = app;
		this._fileName = fileName;
		this._map = this.loadSettings();
	}

	private void saveSettings(HashMap<String, String> map) {
		StringBuilder sb = new StringBuilder();
		for (String key : map.keySet()) {
			String value = map.get(key);
			byte[] bytes = Base64.encode(value.getBytes(), Base64.DEFAULT);
			value = new String(bytes);
			sb.append("key");
			sb.append("=");
			sb.append(value);
			sb.append("\r\n");
		}
		String data = sb.toString();
		try {
			FileOutputStream fs = this._app.openFileOutput(this._fileName, 0);
			OutputStreamWriter sw = new OutputStreamWriter(fs);
			sw.write(data);
		} catch (Exception e) {
			Log.d("File open write failed:", this._fileName);
		}
	}

	private HashMap<String, String> loadSettings() {
		HashMap<String, String> map = new HashMap<String, String>();
		try {
			FileInputStream fs = this._app.openFileInput(this._fileName);
			InputStreamReader ir = new InputStreamReader(fs);
			BufferedReader bs = new BufferedReader(ir);
			String line = null;
			while ((line = bs.readLine()) != null) {
				int idx = line.indexOf("=");
				String key = line.substring(0, idx).trim();
				String value = line.substring(idx + 1).trim();
				byte[] bytes = Base64.decode(value.getBytes(), Base64.DEFAULT);
				value = new String(bytes);
				map.put(key, value);
			}
			bs.close();
			ir.close();
			fs.close();

		} catch (Exception e) {
			Log.d("File open read failed:", this._fileName);
		}
		return map;
	}

	public String get(String key, String defaultValue) {
		String value = null;
		if (this._map.containsKey(key)) {
			value = this._map.get(key);
		} else {
			value = defaultValue;
		}
		return value;
	}

	public void set(String key, String value) {
		this._map.put(key, value);
		this.saveSettings(_map);

	}

}
