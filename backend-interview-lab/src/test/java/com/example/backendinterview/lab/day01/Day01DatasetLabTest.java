package com.example.backendinterview.lab.day01;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

class Day01DatasetLabTest {

    private final Day01DatasetLab lab = new Day01DatasetLab();

    @Test
    void fixedDatasetMetadataAndCountsDoNotChange() {
        assertThat(lab.datasetVersion()).isEqualTo("1.0.0");
        assertThat(lab.count("users")).isEqualTo(12);
        assertThat(lab.count("products")).isEqualTo(15);
        assertThat(lab.count("orders")).isEqualTo(30);
        assertThat(lab.count("order_items")).isEqualTo(50);
    }

    @Test
    void arrayAndArrayListKeepTheSameProductOrder() {
        String[] array = lab.productIdsAsArray();
        List<String> list = lab.productIdsAsArrayList();

        assertThat(array).containsExactlyElementsOf(list);
        assertThat(array[0]).isEqualTo("P001");
        assertThat(array[14]).isEqualTo("P015");
    }

    @Test
    void linearSearchFindsTheSoldOutProductFromTheFixedDataset() {
        Day01DatasetLab.ProductView product = lab.findProductLinear("P015").orElseThrow();

        assertThat(product.name()).isEqualTo("한정판 개발자 머그");
        assertThat(product.status()).isEqualTo("SOLD_OUT");
        assertThat(product.price()).isEqualTo(27_000L);
    }

    @Test
    void invalidArrayNameFailsFast() {
        assertThatThrownBy(() -> lab.count("meta"))
                .isInstanceOf(IllegalArgumentException.class)
                .hasMessageContaining("is not an array field");
    }
}
