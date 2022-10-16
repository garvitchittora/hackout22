package com.example.socialout;

public class Experience {

    private String name;
    private String city;
    private String summary;
    private String videoUrl;
    private String experienceId;

    public Experience(){

    }

    public Experience(String name, String city, String summary, String videoUrl, String experienceId) {
        this.name = name;
        this.city = city;
        this.summary = summary;
        this.videoUrl = videoUrl;
        this.experienceId = experienceId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public String getVideoUrl() {
        return videoUrl;
    }

    public void setVideoUrl(String videoUrl) {
        this.videoUrl = videoUrl;
    }

    public String getExperienceId() {
        return experienceId;
    }

    public void setExperienceId(String experienceId) {
        this.experienceId = experienceId;
    }
}
