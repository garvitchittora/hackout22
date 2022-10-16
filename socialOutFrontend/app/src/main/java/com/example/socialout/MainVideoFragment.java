package com.example.socialout;

import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.viewpager2.adapter.FragmentStateAdapter;
import androidx.viewpager2.widget.ViewPager2;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class MainVideoFragment extends Fragment {

    public static final int MAX_VIDEOS = 20;

    private static class ScreenSlidePagerAdapter extends FragmentStateAdapter {
        public ScreenSlidePagerAdapter(@NonNull FragmentActivity fragmentActivity) {
            super(fragmentActivity);
        }

        @NonNull
        @Override
        public Fragment createFragment(int position) {
            return VideoFragment.newInstance(position);
        }

        @Override
        public int getItemCount() {
            return MAX_VIDEOS;
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_main_video, container, false);
    }

    ViewPager2 viewPager2;

    MainViewModel mainViewModel;
    NavController navController;
    ApiSingleton apiSingleton;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        viewPager2 = view.findViewById(R.id.videoViewPager);

        FragmentStateAdapter stateAdapter = new ScreenSlidePagerAdapter(requireActivity());
        viewPager2.setAdapter(stateAdapter);
//        viewPager2.setOffscreenPageLimit(5);

        mainViewModel = new ViewModelProvider(requireActivity()).get(MainViewModel.class);
        navController = Navigation.findNavController(requireView());
        apiSingleton = ApiSingleton.getInstance(requireActivity());

        fetchVideos();
    }

    String URL_VIDEOS = "/experience";

    private void fetchVideos(){
        apiSingleton.sendGetRequest(URL_VIDEOS, (success, result) -> {
            if(success){
                try {
                    ArrayList<Experience> experiences = new ArrayList<>();
                    JSONArray jsonArray = new JSONArray(result);
                    for(int i=0;i<jsonArray.length();i++){
                        JSONObject jsonObject = jsonArray.getJSONObject(i);
                        Experience experience = new Experience();

                        experiences.add(experience);
                    }
                    mainViewModel.setExpList(experiences);
                } catch (JSONException e) {
                    e.printStackTrace();
                    Log.d("FETCH VIDEOS", "Error: "+e.getMessage());
                }
            } else {
                Log.d("FETCH VIDEOS", result);
            }
        });
    }
}