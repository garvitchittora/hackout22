package com.example.socialout;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.appbar.AppBarLayout;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    ApiSingleton apiSingleton;
    MainViewModel mainViewModel;
    NavController navController;

    AppBarLayout appBarLayout;
    FloatingActionButton filterButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        appBarLayout = findViewById(R.id.appBarLayout);
        filterButton = findViewById(R.id.filter);

        filterButton.setOnClickListener(v -> {
            ArrayList<Experience> experiences = new ArrayList<>();
            experiences.add(new Experience("Hello","Varanasi","City in UP","",""));
            experiences.add(new Experience("Hello 1","Prayagraj","Another City in UP","",""));
            mainViewModel.setExpList(experiences);
        });

        navController = Navigation.findNavController(this, R.id.navHostMain);
        ImageView btnSearch = findViewById(R.id.search);

        btnSearch.setOnClickListener(v -> navController.navigate(R.id.action_mainVideoFragment_to_searchFragment));

        RecyclerView recyclerView = (RecyclerView) findViewById(R.id.rv);
        recyclerView.setHasFixedSize(true);

        LinearLayoutManager horizontalLayout = new LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false);
        recyclerView.setLayoutManager(horizontalLayout);

        apiSingleton = ApiSingleton.getInstance(this);
        mainViewModel = new ViewModelProvider(this).get(MainViewModel.class);
        getStories();

        mainViewModel.getStories().observe(this, users -> {
            StoryAdapter storyAdapter = new StoryAdapter(users, userId -> {

            });
            recyclerView.setAdapter(storyAdapter);
        });

        navController.addOnDestinationChangedListener((navController, navDestination, bundle) -> {
            if(navDestination.getId()==R.id.mainVideoFragment){
                appBarLayout.setVisibility(View.VISIBLE);
                filterButton.setVisibility(View.VISIBLE);
            } else if(navDestination.getId()==R.id.searchFragment){
                appBarLayout.setVisibility(View.GONE);
                filterButton.setVisibility(View.GONE);
            }
        });
    }

    private final String URL_USERS = "";

    private void getStories() {
        apiSingleton.sendGetRequest(URL_USERS, (success, result) -> {
            if (success) {
                try {
                    ArrayList<User> userList = new ArrayList<>();
                    JSONArray jsonArray = new JSONArray(result);
                    for (int i = 0; i < jsonArray.length(); i++) {
                        JSONObject jsonObject = jsonArray.getJSONObject(i);
                        User user = new User();

                        userList.add(user);
                    }
                    mainViewModel.setStoryUserList(userList);
                } catch (JSONException e) {
                    e.printStackTrace();
                    Log.d("GET USER STORY", "Error: " + e.getMessage());
                }

            } else {
                Log.d("GET USER STORY", "Error: " + result);
            }
        });
    }
}