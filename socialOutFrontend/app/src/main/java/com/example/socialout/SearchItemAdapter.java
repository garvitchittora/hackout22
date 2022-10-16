package com.example.socialout;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class SearchItemAdapter extends RecyclerView.Adapter<SearchItemAdapter.ViewHolder> {

    public interface SearchItemInterface{
        void onItemClickListener(String user_id);
    }

    private ArrayList<User> usersList;
    private SearchItemInterface itemInterface;

    public SearchItemAdapter(ArrayList<User> usersList, SearchItemInterface itemInterface){
        this.usersList = usersList;
        this.itemInterface = itemInterface;
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
        }
    }

    @NonNull
    @Override
    public SearchItemAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new ViewHolder(LayoutInflater.from(parent.getContext()).inflate(R.layout.search_list_item, parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull SearchItemAdapter.ViewHolder holder, int position) {

    }

    @Override
    public int getItemCount() {
        return usersList.size();
    }
}
