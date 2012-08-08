package com.poas.ui;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class Http {
	public static HttpResponse sendGetRequest(String endpoint,
			String requestParameters) throws IOException {
		String result = null;
		if (!endpoint.startsWith("http://")) {
			endpoint = "http://" + endpoint;
		}
		String urlStr = endpoint;
		if (requestParameters != null && requestParameters.length() > 0) {
			urlStr += "?" + requestParameters;
		}
		URL url = new URL(urlStr);
		URLConnection conn = url.openConnection();

		String cookie = conn.getHeaderField("set-cookie");

		// Get the response
		InputStreamReader r = new InputStreamReader(conn.getInputStream());
		BufferedReader rd = new BufferedReader(r);
		StringBuffer sb = new StringBuffer();
		String line;
		while ((line = rd.readLine()) != null) {
			sb.append(line);
		}
		rd.close();
		result = sb.toString();
		return new HttpResponse(result, cookie);
	}
}
