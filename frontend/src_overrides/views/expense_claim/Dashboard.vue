<template>
	<BaseLayout :pageTitle="__('Expense Claims')">
		<template #body>
			<div class="flex flex-col mt-5 mb-7 p-4 gap-6">
				<ExpenseClaimSummary />

				<div class="w-full">
					<router-link
						:to="{ name: 'ExpenseClaimFormView' }"
						v-slot="{ navigate }"
					>
						<Button
							@click="navigate"
							variant="solid"
							class="w-full py-4 text-base !bg-[#D4AF37] !text-[#051E24] !font-bold rounded-xl shadow-lg border-none hover:!bg-amber-400 transition cursor-pointer"
							style="background: linear-gradient(135deg, #E6CA65 0%, #D4AF37 50%, #B8860B 100%); color: #051E24;"
						>
							<template #prefix>
								<FeatherIcon name="plus-circle" class="w-5 h-5 mr-1" />
							</template>
							{{ __("Claim an Expense") }}
						</Button>
					</router-link>
				</div>

				<div>
					<div class="text-base sm:text-lg text-white font-bold mb-1 tracking-tight px-1">{{ __("Recent Expenses") }}</div>
					<RequestList
						:component="markRaw(ExpenseClaimItem)"
						:items="myClaims.data"
						:addListButton="true"
						listButtonRoute="ExpenseClaimListView"
					/>
				</div>

				<div>
					<div class="flex flex-row justify-between items-center mb-1 px-1">
						<div class="text-base sm:text-lg text-white font-bold tracking-tight">
							{{ __("Employee Advance Balance") }}
						</div>
						<router-link
							:to="{ name: 'EmployeeAdvanceListView' }"
							class="text-xs sm:text-sm text-[#D4AF37] font-semibold cursor-pointer hover:underline"
						>
							{{ __("View List") }} &rarr;
						</router-link>
					</div>

					<EmployeeAdvanceBalance :items="advanceBalance.data" />
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { markRaw } from "vue"
import { Button, FeatherIcon } from "frappe-ui"

import BaseLayout from "@/components/BaseLayout.vue"
import ExpenseClaimSummary from "@/components/ExpenseClaimSummary.vue"
import RequestList from "@/components/RequestList.vue"
import ExpenseClaimItem from "@/components/ExpenseClaimItem.vue"
import EmployeeAdvanceBalance from "@/components/EmployeeAdvanceBalance.vue"

import { myClaims } from "@/data/claims"
import { advanceBalance } from "@/data/advances"
</script>
