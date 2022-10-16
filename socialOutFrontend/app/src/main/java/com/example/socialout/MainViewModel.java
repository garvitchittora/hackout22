package com.example.socialout;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import java.util.ArrayList;

public class MainViewModel extends ViewModel {

    private final MutableLiveData<User> currentUser;
    private final MutableLiveData<ArrayList<User>> storyUserList;
    private final MutableLiveData<ArrayList<Experience>> expList;

    public MainViewModel() {
        currentUser = new MutableLiveData<>();
        storyUserList = new MutableLiveData<>();
        expList = new MutableLiveData<>();
    }

    public void setCurrentUser(User user) {
        currentUser.setValue(user);
    }

    public LiveData<User> getCurrentUser() {
        return currentUser;
    }

    public void setStoryUserList(ArrayList<User> storyUserList) {
        this.storyUserList.setValue(storyUserList);
    }

    public LiveData<ArrayList<User>> getStories() {
        return storyUserList;
    }

    public void setExpList(ArrayList<Experience> experiences) {
        expList.setValue(experiences);
    }

    public LiveData<ArrayList<Experience>> getExperienceList() {
        return expList;
    }

}
