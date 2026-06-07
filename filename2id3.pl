#!/usr/bin/perl


use MP3::Info;
#use MP3::Info::set_mp3v2tag;

foreach $file (@ARGV) {
  $tag  = get_mp3tag($file);

  $file =~ /([0-9]{4}) (.*) - (.*).mp3/;
  ($year, $title, $artist) = ($1, $2, $3);
  #print "$year, $title, $artist\n";

  $tag->{GENRE}  = "Pop";
  $tag->{ARTIST} = $artist;
  $tag->{TITLE} = $title;
  $tag->{YEAR} = $year;
  set_mp3tag($file, $tag);
}

