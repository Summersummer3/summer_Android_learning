package com.example.layoutt;

import java.security.PublicKey;

import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.ActionBar;
import android.support.v4.app.Fragment;
import android.app.Activity;
import android.app.AlertDialog;
import android.app.AlertDialog.Builder;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnFocusChangeListener;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.os.Build;

public class MainActivity extends Activity implements OnFocusChangeListener{

	
	private Button bt;
	private EditText et1,et2;
	/*通过焦点监听器实现成为焦点时将hint隐藏*/

	
	
	
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		bt = (Button) findViewById(R.id.button1);
		
		et1 = (EditText) findViewById(R.id.editText1);
		et2 = (EditText) findViewById(R.id.editText2);
		
		et1.setTag(et1.getHint().toString());
		et2.setTag(et2.getHint().toString());
		
		et1.setOnFocusChangeListener(this);
        et2.setOnFocusChangeListener(this);
		
        et1.requestFocus();
        
		bt.setOnClickListener(new Button.OnClickListener() {
			
			
			public void onClick(View arg0) {
			  String user_name = et1.getText().toString();
		      String pass_word = et2.getText().toString();
		      
		      et1.setFocusable(true);
		      et2.setFocusable(true);
		      
		      if(user_name.equals("")){
		    	  AlertDialog.Builder builder1 = new AlertDialog.Builder(MainActivity.this);
		    	  builder1.setMessage("用户名不得为空")
		    	     .setCancelable(false)
		    	     .setNegativeButton("OK", new DialogInterface.OnClickListener() {
						
						@Override
						public void onClick(DialogInterface dialog, int id) {
							// TODO Auto-generated method stub
							dialog.cancel();
							et1.requestFocus();
							
						}
					}
					);
		    	  AlertDialog ad1 = builder1.create();
		    	  ad1.show();
		    	  
		     }
		      
		      else if(pass_word.equals("")){           //判断字符串为空不能用null用""
		    	  AlertDialog.Builder builder2 = new AlertDialog.Builder(MainActivity.this);
		    	  builder2.setMessage("密码不能为空")
		    	          .setCancelable(false)
		    	          .setNegativeButton("OK", new DialogInterface.OnClickListener() {
							
							@Override
							public void onClick(DialogInterface dialog, int id) {
								dialog.cancel();
								et2.requestFocus();
								
							}
						});
		    	  AlertDialog ad2 = builder2.create();
		    	  ad2.show();
		    	  
		      }
		      
		      else{
		    	  
		    	  Intent intent = new Intent();
		    	  intent.setClass(MainActivity.this, Table1.class);
		    	  Bundle bd = new Bundle();
		    	  bd.putString("user_name", user_name);
		    	  bd.putString("pass_word", pass_word);
		    	  intent.putExtras(bd);    //extra 和 extra还有activity和activities有区别
		    	  startActivityForResult(intent,0);  //后面一个参数是requestcode。
		      }
		    
			}
		});

	}
	
	@Override
	public void onFocusChange(View v, boolean hasFocus) {
		// TODO Auto-generated method stub
		if(et1.hasFocus()){
			et1.setHint("");
			et2.setHint(et2.getTag().toString());
			Log.i("tag", "焦点在1");
		}
		
		else if(et2.hasFocus()){
			et2.setHint("");
			et1.setHint(et1.getTag().toString());
			Log.i("tag", "焦点在2");
		}
	
		
	}

	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		
		switch(resultCode){
		case RESULT_OK:
			Bundle bundle = data.getExtras();
			et1.setText(bundle.getString("user_name"));
			et2.setText(bundle.getString("pass_word"));
			break;
		default:
			break;
		
		}
	}

	
	


}
