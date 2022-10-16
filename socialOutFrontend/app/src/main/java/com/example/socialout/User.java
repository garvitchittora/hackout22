package com.example.socialout;

public class User {

    private int userId;
    private String name;
    private String emailId;
    private String imageUri;
    private int level;

    public User(){

    }

    public User(int userId, String name, String emailId, String imageUri, int level) {
        this.userId = userId;
        this.name = name;
        this.emailId = emailId;
        this.imageUri = imageUri;
        this.level = level;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmailId() {
        return emailId;
    }

    public void setEmailId(String emailId) {
        this.emailId = emailId;
    }

    public String getImageUri() {
        return imageUri;
    }

    public void setImageUri(String imageUri) {
        this.imageUri = imageUri;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
}
