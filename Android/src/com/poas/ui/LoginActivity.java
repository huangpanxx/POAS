package com.poas.ui;

import com.example.poas.R;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

public class LoginActivity extends Activity implements OnClickListener {
	Button _btn_login = null;
	Button _btn_exit = null;
	TextView _txt_address = null;
	TextView _txt_username = null;
	TextView _txt_password = null;
	CheckBox _checkBox_save;
	Settings _settings = null;

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_login);
		_btn_login = (Button) this.findViewById(R.id.btn_login);
		_btn_login.setOnClickListener(this);
		_btn_exit = (Button) this.findViewById(R.id.btn_exit);
		_btn_exit.setOnClickListener(this);
		_txt_address = (TextView) this.findViewById(R.id.txt_address);
		_txt_username = (TextView) this.findViewById(R.id.txt_username);
		_txt_password = (TextView) this.findViewById(R.id.txt_password);
		_checkBox_save = (CheckBox) this
				.findViewById(R.id.checkBox_savePassword);
		_settings = Settings.instance(this.getApplication());
		String address = _settings.get("address", "10.250.62.6");
		String username = _settings.get("username", "poas");
		String password = _settings.get("password", "poas");
		boolean is_save = Boolean
				.parseBoolean(_settings.get("is_save", "true"));
		_txt_address.setText(address);
		_txt_username.setText(username);
		_checkBox_save.setChecked(is_save);
		if (is_save) {
			_txt_password.setText(password);
		}
	}

	@Override
	public void onClick(View v) {
		if (v == this._btn_exit) {
			this.finish();
		}
		if (v == this._btn_login) {
			login();
		}

	}

	private void login() {
		String username = _txt_username.getText().toString();
		String password = _txt_password.getText().toString();
		String address = _txt_address.getText().toString();
		boolean is_save = _checkBox_save.isChecked();
		// check
		/******/
		// save
		_settings.set("username", username);
		_settings.set("address", address);
		_settings.set("is_save", is_save ? "true" : "false");
		if (is_save) {
			_settings.set("password", password);
		}
		// enter
		Intent intent = new Intent(this, MainActivity.class);
		startActivity(intent);
		this.finish();
	}
}
