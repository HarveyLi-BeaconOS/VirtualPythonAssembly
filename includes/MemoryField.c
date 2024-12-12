#include "stdio.h"
#include "stdlib.h"
#include "math.h"

#define ITEMS_PER_MEMORY_FIELD 64
#define SIZE_PER_ITEM_MEMORY_FIELD 8

char InitalizedMemoryField[4];

int InitMemoryFields(){
    int i;
    for (i = 0; i < 5; i++){
        InitalizedMemoryField[i] = calloc(ITEMS_PER_MEMORY_FIELD, SIZE_PER_ITEM_MEMORY_FIELD);
    }
    return 0;
}