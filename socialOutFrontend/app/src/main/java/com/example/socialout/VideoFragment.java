package com.example.socialout;

import static com.google.android.exoplayer2.Player.REPEAT_MODE_ALL;

import android.net.Uri;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.exoplayer2.ExoPlayer;
import com.google.android.exoplayer2.MediaItem;
import com.google.android.exoplayer2.ui.StyledPlayerView;

import java.util.ArrayList;

public class VideoFragment extends Fragment {

    public VideoFragment() {
        // Required empty public constructor
    }

    private final static String POSITION_PARAM = "POSITION_PARAM";

    public static VideoFragment newInstance(int position) {
        VideoFragment fragment = new VideoFragment();
        Bundle args = new Bundle();
        args.putInt(POSITION_PARAM, position);
        fragment.setArguments(args);
        return fragment;
    }

    private int position = 0;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            position = getArguments().getInt(POSITION_PARAM);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_video, container, false);
    }

    private MainViewModel mainViewModel;
    private Experience experience;
    StyledPlayerView playerView;
    TextView tvCity, tvDescription;
    Button btnBook;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        playerView = view.findViewById(R.id.player_view);
        tvCity = view.findViewById(R.id.tvCity);
        tvDescription = view.findViewById(R.id.tvDesciption);
        btnBook = view.findViewById(R.id.btnBook);

        mainViewModel = new ViewModelProvider(requireActivity()).get(MainViewModel.class);
        mainViewModel.getExperienceList().observe(getViewLifecycleOwner(), experiences -> {
            experience = experiences.get(position);
            updateViews();
        });
    }

    private void updateViews() {
        tvCity.setText(experience.getCity());
        tvDescription.setText(experience.getSummary());

        btnBook.setOnClickListener(v -> {
            Toast.makeText(requireContext(), "Booking the City "+experience.getCity(), Toast.LENGTH_SHORT).show();
        });

        ExoPlayer player = new ExoPlayer.Builder(requireContext()).build();
        playerView.setPlayer(player);
        playerView.setUseController(false);

        player.setMediaItem(MediaItem.fromUri(Uri.parse(experience.getVideoUrl())));
        player.setRepeatMode(REPEAT_MODE_ALL);
        player.prepare();
        player.play();
    }
}