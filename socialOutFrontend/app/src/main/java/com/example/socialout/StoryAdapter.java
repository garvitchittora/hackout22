package com.example.socialout;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class StoryAdapter extends RecyclerView.Adapter<StoryAdapter.ViewHolder>{

    public interface StoryItemClickListener{
        void onStoryItemClick(int userId);
    }

    private ArrayList<User> listData;
    private StoryItemClickListener itemClickListener;

    public StoryAdapter(ArrayList<User> listData, StoryItemClickListener itemClickListener) {
        this.listData = listData;
        this.itemClickListener = itemClickListener;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        LayoutInflater layoutInflater = LayoutInflater.from(parent.getContext());
        View listItem= layoutInflater.inflate(R.layout.story_item, parent, false);
        return new ViewHolder(listItem);
    }

    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        User myListData = listData.get(position);
        holder.imageView.setImageResource(R.drawable.ic_person);
        holder.imageView.setOnClickListener(view -> itemClickListener.onStoryItemClick(myListData.getUserId()));
    }

    @Override
    public int getItemCount() {
        return listData.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        public ImageView imageView;
        public ViewHolder(View itemView) {
            super(itemView);
            this.imageView = (ImageView) itemView.findViewById(R.id.profile_image);
        }
    }
}
