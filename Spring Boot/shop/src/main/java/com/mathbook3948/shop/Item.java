package com.mathbook3948.shop;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Item {
    @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
    Long id;
    String title;
    Integer price;

}